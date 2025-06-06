from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (1, "for_sale"),
    (2, "sold"),
    (3, "pending"),
)


class Medium(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Artist(models.Model):
    name = models.CharField(max_length=254)
    user = models.OneToOneField(User, null=True, blank=True,
                                on_delete=models.SET_NULL)
    mini_bio = models.CharField(max_length=250, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_alt = models.CharField(max_length=254, default="Image of the artist")

    def __str__(self):
        return self.name

    def get_artist_name(self):
        return self.name


class Artwork(models.Model):
    """null equals true and blank equals false forces
    user to choose an artist as the artist when creating or
    updating the artwork but allows field to be set to null
    in case artist is removed from system, preserving data
    integrity for the artwork"""

    title = models.CharField(max_length=254)
    medium = models.ForeignKey(
        "Medium", null=True, blank=True, on_delete=models.SET_NULL
    )
    artist = models.ForeignKey(
        "Artist",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="art",
    )
    dimensions = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    status = models.PositiveSmallIntegerField(choices=STATUS, default=1)
    custom_made = models.BooleanField(default=False)
    custom_orderer = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL
        )
    image_alt = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.title
