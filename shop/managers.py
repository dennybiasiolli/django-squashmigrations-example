from django.db import models
from django.db.models import F


class OrderLineManager(models.Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .annotate(amount=F("product_quantity") * F("product_unit_price"))
        )
