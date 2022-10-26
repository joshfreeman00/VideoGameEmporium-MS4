from django.shortcuts import render, redirect, reverse, get_object_or_404


def display_cart(request):
    ''' A view to render the shopping cart '''

    return render(request, 'cart/shopping_cart.html')
