from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm

# Create your views here.


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(
            request, 'There is nothing in your bag. Add something first.')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
    }

    return render(request, template, context)
