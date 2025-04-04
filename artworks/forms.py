from django import forms
from crispy_forms.helper import FormHelper
from .widgets import CustomClearableFileInput
from .models import Artwork, Artist, Medium


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
