from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm


def all_products(request):
    ''' A view to show all products, on the products page'''

    products = Product.objects.all()
    query = None
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

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'The search criteria is empty!')
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'selected_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'stock/products.html', context)


def product_detail(request, product_id):
    ''' A view to show individual products in detail'''

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'stock/product_detail.html', context)


@login_required
def stock_management(request):
    ''' A view to show all stock '''
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'stock/stock_management.html', context)


@login_required
def add_product(request):
    ''' Add a product to the store '''

    if not request.user.is_superuser:
        messages.error(request, 'You are not authorised to do this.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Stock has been successfully added.')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add stock, please try again.')
    else:
        form = ProductForm()

    template = 'stock/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    ''' Edit a product '''

    if not request.user.is_superuser:
        messages.error(request, 'You are not authorised to do this.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated product successfully')
            return redirect(reverse('stock_management'))
        else:
            messages.error(request, 'Failed to update product. \
                           Please try again.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'Editing {product.name}')

    template = 'stock/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    ''' Deletes the selected stock item '''

    if not request.user.is_superuser:
        messages.error(request, 'You are not authorised to do this.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Stock has been deleted.')
    return redirect(reverse('stock_management'))
