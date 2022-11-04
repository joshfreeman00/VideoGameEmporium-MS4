from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in the cart")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51M0Nn7DBHE5alS31XVTtHAn21EffeMcAiPzTkechOfw3wtCdBb4Yri2LdVkw9TPRrmqoXHj7nJuZeXCDd1UlWVgv00eYhI0nAl',
        'client_secret': 'test secret',
    }

    return render(request, template, context)
