from django import forms
from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    """
    A form for site visitors to send a message,
    associated with the ContactUs model
    """
    class Meta:
        model = ContactUs
        fields = (
            'name',
            'email',
            'phone',
            'subject',
            'message',
        )
