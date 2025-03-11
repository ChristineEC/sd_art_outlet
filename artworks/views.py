from django.shortcuts import render, get_object_or_404
from .models import Artwork


def artwork_for_sale(request):
    """ A view to display all artworks for sale
    (excludes those already sold),
    including sorting by medium """

    artworks = Artwork.objects.filter(status=1)

    context = {
        'artworks': artworks,
    }

    return render(request, 'artworks/gallery.html', context)


def artwork_detail(request, artwork_id):
    """ A view to display an individual
    piece of art, with full details"""

    artwork = get_object_or_404(Artwork, pk=artwork_id)

    context = {
        'artwork': artwork,
    }

    return render(request, 'artworks/artwork_detail.html', context)
