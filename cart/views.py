from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from stock.models import Product


def display_cart(request):
    ''' A view to render the shopping cart '''

    return render(request, 'cart/shopping_cart.html')


def add_to_cart(request, item_id):
    ''' Add a quantity of a product to the cart '''

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})

    if size:
        if item_id in list(cart.keys()):
            if size in cart[item_id]['items_by_size'].keys():
                cart[item_id]['items_by_size'][size] += quantity
            else:
                cart[item_id]['items_by_size'][size] = quantity
        else:
            cart[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {product.name} to the cart.')
            print(messages)

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    ''' Adjust the quantity of a product in the cart '''

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})

    if size:
        if quantity > 0:
            cart[item_id]['item_by_size'][size] = quantity
            messages.info(request, f'Updated {product.name}, size {size.upper()}, to {cart[item_id]["items_by_size"][size]}')
        else:
            del cart[item_id]['item_by_size'][size]
            if not cart[item_id]['item_by_size']:
                cart.pop(item_id)
            messages.info(request, f'Removed {product.name}, size {size.upper()}, from the cart.')
    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.info(request, f'Updated {product.name} quantity to {cart[item_id]}')
        else:
            cart.pop(item_id)
            messages.info(request, f'Removed {product.name} from the cart')

    request.session['cart'] = cart
    return redirect(reverse('display_cart'))


def remove_from_cart(request, item_id):
    ''' Remove a product from the cart '''
    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        cart = request.session.get('cart', {})

        if size:
            del cart[item_id]['item_by_size'][size]
            if not cart[item_id]['item_by_size']:
                cart.pop(item_id)
        else:
            cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
