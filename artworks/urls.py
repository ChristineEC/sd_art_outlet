from django.urls import path
from . import views

urlpatterns = [
    path("", views.artwork_for_sale, name="artworks"),
    path("<artwork_id>/", views.artwork_detail, name="artwork_detail"),
    path("artist/<artist_id>/", views.artist_page, name="artist")
    ]
