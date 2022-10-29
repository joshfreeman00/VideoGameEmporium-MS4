from django.shortcuts import render, redirect, reverse, get_object_or_404


def display_cart(request):
    ''' A view to render the shopping cart '''

    return render(request, 'cart/shopping_cart.html')


def add_to_cart(request, item_id):
    ''' Add a quantity of a product to the cart '''

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)
