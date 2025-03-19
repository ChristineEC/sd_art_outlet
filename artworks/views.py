from django.shortcuts import render, get_object_or_404
from .models import Artwork, Medium, Artist


def artwork_for_sale(request):
    """A view to display all artworks for sale
    (excludes those already sold),
    including sorting by medium"""

    artworks = Artwork.objects.filter(status=1)
    mediums = None

    if request.GET:
        if "medium" in request.GET:
            mediums = request.GET["medium"].split(",")
            artworks = artworks.filter(medium__name__in=mediums)
            mediums = Medium.objects.filter(name__in=mediums)

    context = {
        "artworks": artworks,
        "current_mediums": mediums,
    }

    return render(request, "artworks/gallery.html", context)


def artwork_detail(request, artwork_id):
    """A view to display an individual
    piece of art, with full details"""

    artwork = get_object_or_404(Artwork, pk=artwork_id)

    context = {
        "artwork": artwork,
    }

    return render(request, "artworks/artwork_detail.html", context)


def artist_page(request, artist_id):
    """A view to display an individual artist's page"""

    artists = Artist.object.all()

    if request.GET:
        artist = get_object_or_404(Artist, pk=artist_id)

    context = {"artists", artists}

    return render(request, "artworks/artists/artist.html", context)
