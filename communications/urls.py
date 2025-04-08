from django.urls import path
from . import views

urlpatterns = [
    path("", views.contact_us, name="contact_us"),
    path("custom_request/", views.custom_order_request, name="custom_request"),
    path("events/", views.display_events, name="events"),
]
