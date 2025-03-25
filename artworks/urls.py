from django.urls import path
from . import views

urlpatterns = [
    path("", views.artwork_for_sale, name="artworks"),
    path("<int:artwork_id>/", views.artwork_detail, name="artwork_detail"),
    path('add/', views.add_artwork, name='add_artwork'),
    path("artist/<artist_id>/", views.artist_page, name="artist"),
    ]
