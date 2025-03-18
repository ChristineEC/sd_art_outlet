from django.shortcuts import render, redirect, get_object_or_404, reverse, HttpResponse
from django.contrib import messages
from artworks.models import Artwork


def view_cart(request):
    """A view to show the cart contents page"""

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """Add the specified artwork to the shopping cart"""

    artwork = get_object_or_404(Artwork, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    """Check if item is in cart"""
    if item_id in list(cart.keys()):
        messages.info(
            request,
            f'{artwork.title} by {artwork.artist} is already in your cart!'
        )
    else:
        quantity = 1
        cart[item_id] = quantity
        messages.success(request,
                         f'{artwork.title} has been added to your \
                         shopping cart!')

    request.session['cart'] = cart
    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """Remove the item from the cart"""

    try:
        artwork = get_object_or_404(Artwork, pk=item_id)
        cart = request.session.get("cart", {})
        print ('request received')
        cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        print('there is a problem with this function')
        return HttpResponse(status=500)
