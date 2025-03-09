from django.shortcuts import render
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
