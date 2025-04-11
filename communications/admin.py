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


class CustomOrderRequestAdmin(admin.ModelAdmin):
    """
    Displays relevant model fields in admin
    """
    list_display = (
        "user",
        "name",
        "email",
        "created_at",
        "updated_on",
        "have_read",
        "replied_to_on",
        "artwork_ordered",
        "artwork",
    )


admin.site.register(ContactUs)
admin.site.register(CustomOrderRequest, CustomOrderRequestAdmin)
admin.site.register(Event)
