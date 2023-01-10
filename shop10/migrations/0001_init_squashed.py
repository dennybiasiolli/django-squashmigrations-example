# Generated by Django 4.1.4 on 2023-01-10 14:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True
    replaces = [
        ("shop10", "0001_initial"),
        ("shop10", "0002_customer_is_premium"),
        ("shop10", "0003_shippingaddress"),
        ("shop10", "0004_migrate_shipping_address"),
        ("shop10", "0005_remove_customer_shipping_state"),
        ("shop10", "0006_remove_customer_shipping_province"),
        ("shop10", "0007_remove_customer_shipping_city"),
        ("shop10", "0008_remove_customer_shipping_zip_code"),
        ("shop10", "0009_remove_customer_shipping_address"),
        ("shop10", "0010_remove_customer_shipping_name"),
        ("shop10", "0011_alter_shippingaddress_address_and_more"),
        ("shop10", "0012_order"),
        ("shop10", "0013_order_created_at"),
        ("shop10", "0014_orderline"),
        ("shop10", "0015_alter_customer_user"),
        ("shop10", "0016_customer_customer_type"),
        ("shop10", "0017_migrate_is_premium_to_customer_type"),
        ("shop10", "0018_remove_customer_is_premium"),
        ("shop10", "0019_alter_customer_customer_type"),
        ("shop10", "0020_alter_customer_customer_type"),
        ("shop10", "0021_alter_customer_customer_type"),
        ("shop10", "0022_alter_customer_customer_type"),
        ("shop10", "0023_alter_customer_customer_type"),
        ("shop10", "0024_alter_customer_customer_type"),
        ("shop10", "0025_rename_product_quantity_orderline_quantity"),
        ("shop10", "0026_product"),
    ]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                (
                    "customer_type",
                    models.IntegerField(
                        choices=[
                            (0, "Free"),
                            (1, "Premium"),
                            (2, "Bronze"),
                            (3, "Silver"),
                            (4, "Gold"),
                            (5, "Platinum"),
                            (6, "Diamond"),
                            (10, "Main"),
                        ],
                        default=0,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="shop10_customer",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orders",
                        to="shop10.customer",
                    ),
                ),
            ],
        ),
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
                ("name", models.CharField(max_length=200)),
                ("address", models.CharField(max_length=100)),
                ("zip_code", models.CharField(max_length=10)),
                ("city", models.CharField(max_length=100)),
                ("province", models.CharField(max_length=5)),
                ("state", models.CharField(max_length=50)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="shipping_addresses",
                        to="shop10.customer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("um", models.CharField(max_length=10)),
                ("unit_price", models.FloatField()),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="shop10.customer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderLine",
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
                ("product_name", models.CharField(max_length=100)),
                ("product_um", models.CharField(max_length=10)),
                ("product_unit_price", models.FloatField()),
                ("quantity", models.FloatField()),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lines",
                        to="shop10.order",
                    ),
                ),
            ],
        ),
    ]
