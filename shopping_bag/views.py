from django.shortcuts import render, redirect

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
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
