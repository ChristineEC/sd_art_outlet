from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
                       'order_number',
                       'date',
                       'order_total',
                       'grand_total',
                       )

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'street_address1',
              'street_address2', 'town_or_city', 'state',
              'postcode', 'country', 'order_total',
              'discount', 'grand_total', 'original_cart',
              'stripe_pid',
              )

    list_display = (
        "order_number",
        "date",
        "full_name",
        "order_total",
        "discount",
        "grand_total",
        "original_cart",
        "stripe_pid",
    )
    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
