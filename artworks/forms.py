from django import forms
from .widgets import CustomClearableFileInput
from .models import Artwork


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
            'custom_made',
            'custom_orderer',
            'image_alt',
        )

    image = forms.ImageField(
                             label='Image',
                             required=False,
                             widget=CustomClearableFileInput
                            )
