from django.db import models
from artworks.models import Artwork
from django.contrib.auth.models import User


class ContactUs(models.Model):
    """Stores a single entry of a contact request"""

    class Meta:
        verbose_name_plural = "Contact Us Messages"

    name = models.CharField(max_length=40, blank=False)
    email = models.EmailField(blank=False)
    phone = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=False)
    read = models.BooleanField(default=False)
    replied_to_on = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Message from {self.name}, {self.email}, phone: {self.phone}"


class CustomOrderRequest(models.Model):
    """Stores a single entry of a custom order request"""

    user = models.ForeignKey(
            User, on_delete=models.CASCADE,
            related_name="custom_order_requests")
    name = models.CharField(max_length=255, default="")
    email = models.EmailField(blank=False)
    phone = models.IntegerField(null=True, blank=True)
    message = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    have_read = models.BooleanField(default=False)
    replied_to_on = models.DateTimeField(null=True, blank=True)
    artwork_ordered = models.BooleanField(default=False)
    artwork = models.ForeignKey(
        Artwork, null=True, blank=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.user.username


class Event(models.Model):
    """Stores a single entry of an event"""

    name = models.CharField(max_length=255, null=False, blank=False)
    location = models.CharField(max_length=255, null=False, blank=False)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(blank=False, null=False)
    specifics = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(null=True, blank=True)
    publish = models.BooleanField(default=False)
    free_entrance = models.BooleanField(default=False)
