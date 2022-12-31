from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile

import stripe

import json
import time


class StripeWH_Handler:
    """
    Handle Stripe webhooks
    Credits to Boutique Ado Walkthrough
    """
    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """
        Send order confiramtion email
        """
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email])

    def handle_event(self, event):
        """
        Handle a unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook recieved: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        # Get charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)

        # Clean data in the shipping details fields
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile information when save_info checkbox is checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_full_name = shipping_details.name,
                profile.default_street_address1 = shipping_details.address.line1,
                profile.default_street_address2 = shipping_details.address.line2,
                profile.default_postcode = shipping_details.address.postal_code,
                profile.default_town_or_city = shipping_details.address.city,
                profile.default_county = shipping_details.address.state,
                profile.default_country = shipping_details.address.country,
                profile.default_phone_number = shipping_details.phone,
                profile.default_email = billing_details.email,
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    county__iexact=shipping_details.address.state,
                    country__iexact=shipping_details.address.country,
                    phone_number__iexact=shipping_details.phone,
                    email__iexact=billing_details.email,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook recieved:\
                    {event["type"]} | SUCCESS: Verified \
                    order exists in the database.',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                        full_name=shipping_details.name,
                        user_profile=profile,
                        street_address1=shipping_details.address.line1,
                        street_address2=shipping_details.address.line2,
                        postcode=shipping_details.address.postal_code,
                        town_or_city=shipping_details.address.city,
                        county=shipping_details.address.state,
                        country=shipping_details.address.country,
                        phone_number=shipping_details.phone,
                        email=billing_details.email,
                        original_bag=bag,
                        stripe_pid=pid,
                    )
                for item_id, item_data in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook recieved: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]} | SUCCESS:\
                Order created in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)
