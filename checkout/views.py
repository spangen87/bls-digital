from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from shopping_bag.contexts import bag_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Your payment cannot be processed \
            Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'country': request.POST['country'],
            'phone_number': request.POST['phone_number'],
            'email': request.POST['email'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                except Product.DoesNotExist:
                    messsage.error(request, (
                        'One of the products was not found.'
                        'Contact us for assistance.'
                    ))
                    order.delete()
                    return redirect(reverse('view_bag'))
            request.session['save_info'] = 'save-info' in request.POST
            # Send confirmation email
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

            # Send mail to store about new order
            store_email = settings.DEFAULT_FROM_EMAIL
            subject = 'You got a new order!'
            body = f'Order from: {order.full_name}. Login to admin dashboard \
                to handle it. Order number: {order.order_number}'
            send_mail(subject, body, store_email, [store_email])    
            return redirect(
                reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Check your information and try again.')
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(
                request, 'There is nothing in your bag. Add something first.')
            return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            order_form = OrderForm(initial={
                'full_name': profile.default_full_name,
                'street_address1': profile.default_street_address1,
                'street_address2': profile.default_street_address2,
                'postcode': profile.default_postcode,
                'town_or_city': profile.default_town_or_city,
                'county': profile.default_county,
                'country': profile.default_country,
                'phone_number': profile.default_phone_number,
                'email': profile.default_email,
            })
        except UserProfile.DoesNotExist:
            order_form = OrderForm()
    else:
        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing.')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successfull checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    # Save user info to profile
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

        if save_info:
            profile_data = {
                'default_full_name': order.full_name,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_county': order.county,
                'default_country': order.country,
                'default_phone_number': order.phone_number,
                'default_email': order.email,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order placed successfully! \
        Your order number is {order.order_number}. A email confiramtion \
            will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
