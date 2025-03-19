from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from artworks.models import Artwork


def cart_contents(request):

    cart_items = []
    total = 0
    artwork_count = 0
    cart = request.session.get("cart", {})

    for item_id, item_data in cart.items():

        artwork = get_object_or_404(Artwork, pk=item_id)
        total += artwork.price
        artwork_count += item_data
        cart_items.append(
            {
                "item_id": item_id,
                "quantity": item_data,
                "artwork": artwork,
            }
        )

    grand_total = total

    context = {
        "cart_items": cart_items,
        "grand_total": grand_total,
        "artwork_count": artwork_count,
    }

    return context
