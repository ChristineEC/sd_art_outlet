from django.contrib import admin
from .models import Medium, Artist, Artwork


# class ArtworkAdmin(admin.ModelAdmin):
#     list_display = (
#         'title',
#         'artist',
#         'medium',
#         'dimensions',
#         'price',
#         'image',
#         'status',
#         'custom_made',
#     )


admin.site.register(Medium)
admin.site.register(Artist)
admin.site.register(Artwork)
