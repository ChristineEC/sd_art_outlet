from django.db import models


class ContactUs(models.Model):
    """Stores a single entry of a contact request"""
    name = models.CharField(max_length=40, blank=False)
    email = models.EmailField(blank=False)
    phone = models.IntegerField(null=True, blank=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=False)
    read = models.BooleanField(default=False)
    replied_to = models.BooleanField(default=False)

    def __str__(self):
        return f'Message from {self.name}, {self.email}, phone: {self.phone}'
