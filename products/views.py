from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.core.paginator import Paginator
from .models import Product, Category
from .forms import ProductForm

# Create your views here.


def all_products(request):
    """
    A view to show alls products, including sorting and search
    The base structure comes from Boutique Ado walkthrough project
    """

    products = Product.objects.all()
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    result = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            page_obj = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            page_obj = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'search' in request.GET:
            result = request.GET['search']
            if not result:
                messages.error(
                    request, "You need to enter something to search for.")
                return redirect(reverse('products'))

            search_results = Q(
                name__icontains=result) | Q(description__icontains=result)
            page_obj = products.filter(search_results)

    current_sorting = f'{sort}_{direction}'

    context = {
        'page_obj': page_obj,
        'search_term': result,
        'current_categories': categories,
        'current_sorting': current_sorting,
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


@login_required
def add_product(request):
    """
    Add product to the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product.\
                 Please check that the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Edit a existing product
    """
    if not request.user.is_superuser:
        messages.error(request, 'Only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated!')
            return redirect(reverse('product_detail', args=[product_id]))
        else:
            messages.error(request, 'Update failed.\
                 Please check that the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Delete product
    """
    if not request.user.is_superuser:
        messages.error(request, 'Only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
