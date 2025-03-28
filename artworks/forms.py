from django import forms
from .widgets import CustomClearableFileInput
from .models import Artwork, Artist, Medium


class ArtworkForm(forms.ModelForm):
    """
    Form for adding and updating
    Artworks on the front end
    """

    class Meta:
        model = Artwork
        fields = '__all__'

    image = forms.ImageField(
                             label='Image',
                             required=False,
                             widget=CustomClearableFileInput
                            )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        mediums = Medium.objects.all()
        artists = Artist.objects.all()
        friendly_names = [(m.id, m.get_friendly_name()) for m in mediums]
        artist_names = [(a.id, a.get_artist_name()) for a in artists]

        self.fields['medium'].choices = friendly_names
        self.fields['artist'].choices = artist_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = "border-black rounded-0"
