from django.urls import path
from . import views

urlpatterns = [
    path("", views.artwork_for_sale, name="gallery"),
    ]
