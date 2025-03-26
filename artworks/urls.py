from django.urls import path
from . import views

urlpatterns = [
    path("", views.artwork_for_sale, name="artworks"),
    path("<int:artwork_id>/", views.artwork_detail, name="artwork_detail"),
    path('add/', views.add_artwork, name='add_artwork'),
    path('artists/', views.all_artists, name='all_artists'),
    path('artist/<int:artist_id>/', views.artist_page, name="artist_page"),
    path('delete/<int:artwork_id>/', views.delete_artwork,
         name='delete_artwork'),
    path('gallery/', views.full_gallery, name='full_gallery'),
    path('update/<int:artwork_id>/', views.update_artwork,
         name='update_artwork'),
    ]
