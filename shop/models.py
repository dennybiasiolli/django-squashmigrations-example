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
    shipping_name = models.CharField(max_length=100)
    shipping_address = models.CharField(max_length=50)
    shipping_zip_code = models.CharField(max_length=10)
    shipping_city = models.CharField(max_length=50)
    shipping_province = models.CharField(max_length=5)
    shipping_state = models.CharField(max_length=20)
