from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
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
        messages.error(
            request,
            f'{artwork.title} by {artwork.artist} is already in your cart!'
        )
    else:
        quantity = 1
        cart[item_id] = quantity

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)
