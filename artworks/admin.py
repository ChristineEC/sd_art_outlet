from django.contrib import admin
from .models import Medium, Artist, Artwork


class ArtworkAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "artist",
        "medium",
        "dimensions",
        "price",
        "image",
        "image_alt",
        "status",
        "custom_made",
    )


class MediumAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
    )


class ArtistAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "user",
        "image",
    )


admin.site.register(Medium, MediumAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Artwork, ArtworkAdmin)
