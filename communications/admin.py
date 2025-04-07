from django.contrib import admin
from .models import ContactUs, CustomOrderRequest, NewsletterSignup


class NewsletterSignupAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "added_to_list",
    )

admin.site.register(ContactUs)
admin.site.register(CustomOrderRequest)
admin.site.register(NewsletterSignup, NewsletterSignupAdmin)
