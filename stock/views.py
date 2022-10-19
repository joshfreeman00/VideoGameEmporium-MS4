from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm


def add_product(request):
    ''' Add a product to the store '''

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
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

def edit_product(request, product_id):
    ''' Edit a product '''
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated product successfully')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please try again.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'Editing {product.name}')

    template = 'stock/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)
