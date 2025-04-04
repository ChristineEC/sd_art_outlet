from django import forms
from crispy_forms.helper import FormHelper
from .models import ContactUs, CustomOrderRequest


class ContactUsForm(forms.ModelForm):
    """
    A form for site visitors to send a message,
    associated with the ContactUs model
    """
    class Meta:
        model = ContactUs
        fields = (
            "name",
            "email",
            "phone",
            "subject",
            "message",
        )

    def __init__(self, *args, **kwargs):
        """Add placeholders, remove auto-generated
        labels, and set autofocus on the first field"""

        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        placeholders = {
            "name": "Name",
            "email": "Email",
            "phone": "Phone Number",
            "subject": "Subject",
            "message": "Message",
        }

        self.fields["name"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f"{placeholders[field]} *"
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs["placeholder"] = placeholder
        self.fields[field].widget.attrs["class"] = "contact-form-input"
        self.helper.form_show_labels = False


class CustomOrderRequestForm(forms.ModelForm):
    """
    A form for a logged in user to send a
    custom order request
    """
    class Meta:
        model = CustomOrderRequest
        fields = (
            "name",
            "email",
            "phone",
            "message",
        )

    def __init__(self, *args, **kwargs):
        """Add placeholders, remove auto-generated
        labels, and set autofocus on the first field"""

        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        placeholders = {
            "name": "Name",
            "email": "Email",
            "phone": "Phone Number",
            "message": "Message",
        }

        self.fields["name"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f"{placeholders[field]} *"
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs["placeholder"] = placeholder
        self.fields[field].widget.attrs[
                "class"] = "custom-order-request-form-input"
        self.helper.form_show_labels = False
