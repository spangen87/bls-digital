from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_shopping_bag(request):
    """
    A view to render the shopping bag
    """
    return render(request, 'shopping_bag/shopping_bag.html')


def add_to_bag(request, item_id):
    """
    Add product to shopping bag with specified quantity
    From Boutique Ado walkthrough
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        if product.quantity > quantity:
            bag[item_id] += quantity
            product.quantity -= quantity
            messages.success(
                request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            messages.error(request, 'There is not enough stock!')

    else:
        if product.quantity > quantity:
            bag[item_id] = quantity
            product.quantity -= quantity
            messages.success(request, f'Added {product.name} to your bag')
        else:
            messages.error(request, 'There is not enough stock!')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    Add product to shopping bag with specified quantity
    From Boutique Ado walkthrough
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = request.POST.get('quantity')
    if quantity.isdigit():
        quantity = int(request.POST.get('quantity'))
    else:
        messages.error(request, 'Please check that you entered a valid input')
        return redirect(reverse('view_shopping_bag'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_shopping_bag'))


def remove_from_bag(request, item_id):
    """
    Remove item from shopping bag
    """

    product = get_object_or_404(Product, pk=item_id)

    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
