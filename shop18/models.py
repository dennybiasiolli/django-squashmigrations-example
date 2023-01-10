from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import F, Sum
from django.utils.functional import cached_property

from .managers import OrderLineManager


class Customer(models.Model):
    class CustomerType(models.IntegerChoices):
        FREE = 0
        PREMIUM = 1
        BRONZE = 2
        SILVER = 3
        GOLD = 4
        PLATINUM = 5
        DIAMOND = 6
        MAIN = 10

    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        unique=True,
        related_name="shop18_customer",
    )
    customer_type = models.IntegerField(
        choices=CustomerType.choices,
        default=CustomerType.FREE,
    )


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


class Product(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="products"
    )
    name = models.CharField(max_length=100)
    um = models.CharField(max_length=10)
    unit_price = models.FloatField()


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
    created_at = models.DateTimeField(auto_now_add=True)

    @cached_property
    def total_amount(self):
        aggregation = (
            self.lines.all()
            .annotate(amount=F("quantity") * F("product_unit_price"))
            .aggregate(total_amount=Sum("amount"))
        )
        return aggregation["total_amount"]

    def copy_shipping_address(self, shipping_address: ShippingAddress):
        self.shipping_name = shipping_address.name
        self.shipping_address = shipping_address.address
        self.shipping_zip_code = shipping_address.zip_code
        self.shipping_city = shipping_address.city
        self.shipping_province = shipping_address.province
        self.shipping_state = shipping_address.state


class OrderLine(models.Model):
    objects = OrderLineManager()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="lines")
    product_name = models.CharField(max_length=100)
    product_um = models.CharField(max_length=10)
    product_unit_price = models.FloatField()
    quantity = models.FloatField()

    def copy_product(self, product: Product):
        self.product_name = product.name
        self.product_um = product.um
        self.product_unit_price = product.unit_price
