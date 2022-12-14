from django.contrib.auth import get_user_model
from django.db import models


class Customer(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        unique=True,
        related_name="customer",
    )
    is_premium = models.BooleanField(default=False)


class ShippingAddress(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="shipping_addresses"
    )
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=5)
    state = models.CharField(max_length=50)


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="orders"
    )
    shipping_name = models.CharField(max_length=200, blank=True)
    shipping_address = models.CharField(max_length=100, blank=True)
    shipping_zip_code = models.CharField(max_length=10, blank=True)
    shipping_city = models.CharField(max_length=100, blank=True)
    shipping_province = models.CharField(max_length=5, blank=True)
    shipping_state = models.CharField(max_length=50, blank=True)

    def copy_shipping_address(self, shipping_address: ShippingAddress):
        self.shipping_name = shipping_address.name
        self.shipping_address = shipping_address.address
        self.shipping_zip_code = shipping_address.zip_code
        self.shipping_city = shipping_address.city
        self.shipping_province = shipping_address.province
        self.shipping_state = shipping_address.state
