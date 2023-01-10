# Generated by Django 4.1.4 on 2022-12-14 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shop05", "0011_alter_shippingaddress_address_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("shipping_name", models.CharField(blank=True, max_length=200)),
                ("shipping_address", models.CharField(blank=True, max_length=100)),
                ("shipping_zip_code", models.CharField(blank=True, max_length=10)),
                ("shipping_city", models.CharField(blank=True, max_length=100)),
                ("shipping_province", models.CharField(blank=True, max_length=5)),
                ("shipping_state", models.CharField(blank=True, max_length=50)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orders",
                        to="shop05.customer",
                    ),
                ),
            ],
        ),
    ]
