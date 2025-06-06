from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """Allows a user to update their profile"""
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """Add placeholders, remove auto-generated
        labels, and set autofocus on the first field"""

        super().__init__(*args, **kwargs)
        placeholders = {
            "default_phone_number": "Phone Number",
            "default_street_address1": "Street Address 1",
            "default_street_address2": "Street Address 2",
            "default_town_or_city": "City",
            "default_state": "State or Locality",
            "default_postcode": "Zip Code",
            "default_country": "Country",
        }

        self.fields["default_phone_number"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if field != "default_country":
                if self.fields[field].required:
                    placeholder = f"{placeholders[field]} *"
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].widget.attrs["class"] = "profile-form-input"
            self.fields[field].label = False
