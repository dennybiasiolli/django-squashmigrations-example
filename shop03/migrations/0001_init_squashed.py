# Generated by Django 4.1.4 on 2023-01-10 14:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True
    replaces = [
        ("shop03", "0001_initial"),
        ("shop03", "0002_customer_is_premium"),
        ("shop03", "0003_shippingaddress"),
        ("shop03", "0004_migrate_shipping_address"),
        ("shop03", "0005_remove_customer_shipping_state"),
        ("shop03", "0006_remove_customer_shipping_province"),
        ("shop03", "0007_remove_customer_shipping_city"),
        ("shop03", "0008_remove_customer_shipping_zip_code"),
        ("shop03", "0009_remove_customer_shipping_address"),
        ("shop03", "0010_remove_customer_shipping_name"),
        ("shop03", "0011_alter_shippingaddress_address_and_more"),
        ("shop03", "0012_order"),
        ("shop03", "0013_order_created_at"),
        ("shop03", "0014_orderline"),
        ("shop03", "0015_alter_customer_user"),
        ("shop03", "0016_customer_customer_type"),
        ("shop03", "0017_migrate_is_premium_to_customer_type"),
        ("shop03", "0018_remove_customer_is_premium"),
        ("shop03", "0019_alter_customer_customer_type"),
        ("shop03", "0020_alter_customer_customer_type"),
        ("shop03", "0021_alter_customer_customer_type"),
        ("shop03", "0022_alter_customer_customer_type"),
        ("shop03", "0023_alter_customer_customer_type"),
        ("shop03", "0024_alter_customer_customer_type"),
        ("shop03", "0025_rename_product_quantity_orderline_quantity"),
        ("shop03", "0026_product"),
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
                        related_name="shop03_customer",
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
                        to="shop03.customer",
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
                        to="shop03.customer",
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
                        to="shop03.customer",
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
                        to="shop03.order",
                    ),
                ),
            ],
        ),
    ]
