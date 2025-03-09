from django.contrib import admin
from .models import Medium, Artist, Artwork


# class ArtworkAdmin(admin.ModelAdmin):
#     list_display = (
#         'title',
#         'artist',
#         'medium',
#         'dimensions',
#         'note',
#         'price',
#         'image',
#         'status',
#         'made_for',
#     )


admin.site.register(Medium)
admin.site.register(Artist)
admin.site.register(Artwork)
