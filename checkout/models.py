import uuid

from django.db import models
from django.db.models import Sum

from django_countries.fields import CountryField

from artworks.models import Artwork
from profiles.models import UserProfile


class Order(models.Model):
    order_number = models.CharField(
                                    max_length=32,
                                    null=False,
                                    editable=False)
    user_profile = models.ForeignKey(
                                     UserProfile,
                                     on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name="orders")
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=50, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    country = CountryField(blank_label="Country *", null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    discount = models.DecimalField(max_digits=6, decimal_places=2,
                                   null=False, default=0)
    grand_total = models.DecimalField(max_digits=7, decimal_places=2,
                                      null=False, default=0)
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False,
                                  blank=False, default='')

    def _generate_order_number(self):
        """Generate a random, unique order
        number using UUID"""
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """Update the grand total of the order each time
        a lineitem is added to the order"""

        self.order_total = (
            self.lineitems.aggregate(Sum("lineitem_total"))[
                "lineitem_total__sum"]
            or 0
        )
        self.grand_total = self.order_total
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the orginal save method to set the order
        number if it hasn't been set already
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    artwork = models.ForeignKey(Artwork, null=False, blank=False,
                                on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=7,
                                         decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total
        """
        self.lineitem_total = self.artwork.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.artwork.title} on order number \
                {self.order.order_number}'
