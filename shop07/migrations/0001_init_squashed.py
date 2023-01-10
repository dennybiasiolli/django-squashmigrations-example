# Generated by Django 4.1.4 on 2023-01-10 14:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True
    replaces = [
        ("shop07", "0001_initial"),
        ("shop07", "0002_customer_is_premium"),
        ("shop07", "0003_shippingaddress"),
        ("shop07", "0004_migrate_shipping_address"),
        ("shop07", "0005_remove_customer_shipping_state"),
        ("shop07", "0006_remove_customer_shipping_province"),
        ("shop07", "0007_remove_customer_shipping_city"),
        ("shop07", "0008_remove_customer_shipping_zip_code"),
        ("shop07", "0009_remove_customer_shipping_address"),
        ("shop07", "0010_remove_customer_shipping_name"),
        ("shop07", "0011_alter_shippingaddress_address_and_more"),
        ("shop07", "0012_order"),
        ("shop07", "0013_order_created_at"),
        ("shop07", "0014_orderline"),
        ("shop07", "0015_alter_customer_user"),
        ("shop07", "0016_customer_customer_type"),
        ("shop07", "0017_migrate_is_premium_to_customer_type"),
        ("shop07", "0018_remove_customer_is_premium"),
        ("shop07", "0019_alter_customer_customer_type"),
        ("shop07", "0020_alter_customer_customer_type"),
        ("shop07", "0021_alter_customer_customer_type"),
        ("shop07", "0022_alter_customer_customer_type"),
        ("shop07", "0023_alter_customer_customer_type"),
        ("shop07", "0024_alter_customer_customer_type"),
        ("shop07", "0025_rename_product_quantity_orderline_quantity"),
        ("shop07", "0026_product"),
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
                        related_name="shop07_customer",
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
                        to="shop07.customer",
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
                        to="shop07.customer",
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
                        to="shop07.customer",
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
                        to="shop07.order",
                    ),
                ),
            ],
        ),
    ]
