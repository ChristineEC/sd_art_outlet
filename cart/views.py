from django.shortcuts import render


def view_cart(request):
    """A view to show the cart contents page"""

    return render(request, 'cart/cart.html')