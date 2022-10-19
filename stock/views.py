from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm

def add_product(request):
    ''' Add a product to the store '''
    form = ProductForm()
    template = 'stock/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
