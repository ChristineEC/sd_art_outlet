from django.db import models

STATUS = (
    (1, "for_sale"),
    (2, "sold"),
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
    bio = models.TextField(null=True, blank=True)
    selfie_url = models.URLField(max_length=1024, null=True, blank=True)
    selfie = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Artwork(models.Model):
    title = models.CharField(max_length=254)
    medium = models.ForeignKey('Medium', null=True, blank=True,
                               on_delete=models.SET_NULL)
    artist = models.ForeignKey('Artist', null=True, blank=True,
                               on_delete=models.SET_NULL)
    dimensions = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    status = models.PositiveSmallIntegerField(choices=STATUS, default=1)
    custom_made = models.BooleanField(default=False)

    def __str__(self):
        return self.title
