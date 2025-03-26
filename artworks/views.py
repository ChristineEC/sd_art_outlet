from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages

from .models import Artwork, Medium, Artist
from .forms import ArtworkForm


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


def add_artwork(request):
    """Add an artwork from the front end"""
    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            if not request.FILES:
                artwork = form.save(commit=False)
                artwork.status = 3
                form.save()
                messages.success(request,
                    ('Your artwork has been saved with a status of pending. '
                     'You can change the status to "for-sale" or "sold" or "past work" '
                     'when you attach an image file. '
                     'This is to prevent artworks appearing on the site with no image! '
                     'The object can be accessed from your artist page.'
                    ))
                return redirect(reverse('add_artwork'))
            else:
                form.save()
                print('the artwork has an image')
                messages.success(request, 'Successfully added artwork!')
                return redirect(reverse('add_artwork'))
        else:
            messages.error(request, (
                'Failed to add product. Please ensure the form is valid'))
    else:
        form = ArtworkForm()

    template = 'artworks/add_artwork.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def artist_page(request, artist_id):
    """A view to display an individual artist's page"""

    artist = get_object_or_404(Artist, pk=artist_id)
    artworks = Artwork.objects.filter(artist=artist)
    template = 'artworks/artist.html'

    context = {"artist": artist, 'artworks': artworks}

    return render(request, template, context)


def all_artists(request):
    """
    View to display all current artists"
    """
    artists = Artist.objects.all()
    template = 'artworks/artists.html'
    context = {"artists": artists}

    return render(request, template, context)
