from django.contrib import admin
from .models import ContactUs, CustomOrderRequest, Event


class EventAdmin(admin.ModelAdmin):
    """User friendly display in the admin panel"""
    list_display = (
        "name",
        "location",
        "start_date",
        "end_date",
        "specifics",
        "image",
        "publish",
        "free_entrance",
    )
    ordering = ("-start_date", "end_date",)


admin.site.register(ContactUs)
admin.site.register(CustomOrderRequest)
admin.site.register(Event)
