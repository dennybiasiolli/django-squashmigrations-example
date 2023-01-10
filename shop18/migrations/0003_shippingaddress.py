# Generated by Django 4.1.4 on 2022-12-14 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shop18", "0002_customer_is_premium"),
    ]

    operations = [
        migrations.CreateModel(
            name="ShippingAddress",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=50)),
                ("zip_code", models.CharField(max_length=10)),
                ("city", models.CharField(max_length=50)),
                ("province", models.CharField(max_length=5)),
                ("state", models.CharField(max_length=20)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="shipping_addresses",
                        to="shop18.customer",
                    ),
                ),
            ],
        ),
    ]
