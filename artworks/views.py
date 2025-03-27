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

    return render(request, "artworks/shop.html", context)

def full_gallery(request):
    """A view to display all artworks for sale
    (excludes those already sold),
    including sorting by medium"""

    artworks = Artwork.objects.all()
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
    if request.method == "POST":
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            if not request.FILES:
                artwork = form.save(commit=False)
                artwork.status = 3
                artwork = form.save()
                messages.success(
                    request,
                    (
                        'Artwork saved with status "pending" because '
                        "no image was attached. You can access the object from "
                        "the artist page to update it with an image and change "
                        "the status so it can appear publicly."
                    ),
                )
                return redirect(reverse("artwork_detail", args=[artwork.id]))
            else:
                artwork = form.save()
                messages.success(request, "Successfully added artwork!")
                return redirect(reverse("artwork_detail", args=[artwork.id]))
        else:
            messages.error(
                request,
                (
                    "Failed to add artwork. Please ensure the form is valid"
                )
            )
    else:
        form = ArtworkForm()

    template = "artworks/add_artwork.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


def update_artwork(request, artwork_id):
    """Update an artwork"""
    artwork = get_object_or_404(Artwork, pk=artwork_id)
    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES, instance=artwork)
        if form.is_valid:
            artwork = form.save()
            messages.success(request, f'{artwork.title} has been updated')
            return redirect(reverse('artwork_detail', args=[artwork.id]))
        else:
            messages.error(request, (
                    'Failed to update the artwork. '
                    'Please ensure the form is valid.'))
    else:
        form = ArtworkForm(instance=artwork)
        messages.info(request, f'Your are updating {artwork.title}')

    template = 'artworks/update_artwork.html'
    context = {
        'form': form,
        'artwork': artwork,
    }

    return render(request, template, context)


def delete_artwork(request, artwork_id):
    """Delete an artwork from the shop and gallery"""
    artwork = get_object_or_404(Artwork, pk=artwork_id)
    artwork.delete()
    messages.success(request, 'Artwork deleted!')
    return redirect(reverse('artworks'))


# -------------------------------Artist section
def all_artists(request):
    """
    View to display all current artists"
    """
    artists = Artist.objects.all()
    template = 'artworks/artists.html'
    context = {"artists": artists}

    return render(request, template, context)


def artist_page(request, artist_id):
    """
    A view to display an individual artist's page
    """
    artist = get_object_or_404(Artist, pk=artist_id)
    artworks = Artwork.objects.filter(artist=artist)
    template = 'artworks/artist.html'

    context = {"artist": artist, 'artworks': artworks}

    return render(request, template, context)

def artist_add_art(request, artist_id):
    """View to allow artists to add an artwork as artist"""
    if request.method == "GET":
        artist = get_object_or_404(Artist, pk=artist_id)
        form = ArtworkForm()
    if request.method == "POST":
        print(artist_id)
        artist = get_object_or_404(Artist, pk=artist_id)
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            artwork = form.save(commit=False)
            artwork.artist = artist
            artwork.status = 3
            artwork = form.save()
            messages.success(
                request,
                (
                    "Your artwork has been saved with a status of "
                    "'pending' to allow you to review its online "
                    "appearance before publishing. Once you are "
                    "satisfied with its appearance, you can "
                    "update the object's status from this page "
                )
            )
            return redirect(reverse("artist_page", args=[artist.id]))
        else:
            messages.error(
                request,
                ("Failed to add artwork. Please ensure the form is valid")
            )
    else:
        form = ArtworkForm()

    template = "artworks/artist_add_art.html"
    context = {
        "form": form,
        "artist": artist,
    }

    return render(request, template, context)
