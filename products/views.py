from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.


def all_products(request):
    """
    A view to show alls products, including sorting and search
    The base structure comes from Boutique Ado walkthrough project
    """

    products = Product.objects.all()
    result = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category']
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'search' in request.GET:
            result = request.GET['search']
            if not result:
                messages.error(
                    request, "You need to enter something to search for.")
                return redirect(reverse('products'))

            search_results = Q(name__icontains=result) | Q(description__icontains=result)
            products = products.filter(search_results)

    context = {
        'products': products,
        'search_term': result,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    A view to show product details of a specific product
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
