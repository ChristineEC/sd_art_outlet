from django import forms
from .widgets import ClearableFileInput
from .models import Artwork, Medium, Artist


class ArtworkForm(forms.ModelForm):
    """
    Form for adding and updating
    Artworks on the front end.)
    """

    class Meta:
        model = Artwork
        fields = (
            'title',
            'medium',
            'artist',
            'dimensions',
            'price',
            'image',
            'status',
            'image_alt',
        )

    image = forms.ImageField(
        label='Image', required=False, widget=ClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        mediums = Medium.objects.all()
        artists = Artist.objects.all()
        friendly_names = [(m.id, m.get_friendly_name()) for m in mediums]

        self.fields["medium"].choices = friendly_names
