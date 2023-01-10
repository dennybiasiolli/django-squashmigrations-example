# Generated by Django 4.1.7 on 2023-02-24 10:07

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

from shop10.models import Customer


def forward_func_0004(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    CustomerModel = apps.get_model("shop10", "Customer")
    customers = CustomerModel.objects.using(db_alias).all()
    for customer in customers:
        customer.shipping_addresses.create(
            name=customer.shipping_name,
            address=customer.shipping_address,
            zip_code=customer.shipping_zip_code,
            city=customer.shipping_city,
            province=customer.shipping_province,
            state=customer.shipping_state,
        )


def backward_func_0004(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    CustomerModel = apps.get_model("shop10", "Customer")
    customers = CustomerModel.objects.using(db_alias).all()
    for customer in customers:
        shipping_address = customer.shipping_addresses.last()
        if shipping_address:
            customer.shipping_name = shipping_address.name
            customer.shipping_address = shipping_address.address
            customer.shipping_zip_code = shipping_address.zip_code
            customer.shipping_city = shipping_address.city
            customer.shipping_province = shipping_address.province
            customer.shipping_state = shipping_address.state
            customer.save()


def forward_func_0017(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    CustomerModel = apps.get_model("shop10", "Customer")
    customers = CustomerModel.objects.using(db_alias).all()
    for customer in customers:
        customer.customer_type = (
            Customer.CustomerType.PREMIUM
            if customer.is_premium
            else Customer.CustomerType.FREE
        )


def backward_func_0017(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    CustomerModel = apps.get_model("shop10", "Customer")
    customers = CustomerModel.objects.using(db_alias).all()
    for customer in customers:
        is_premium = customer.customer_type == Customer.CustomerType.PREMIUM
        customer.is_premium = is_premium
        customer.save()


class Migration(migrations.Migration):

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
                ("shipping_name", models.CharField(max_length=100)),
                ("shipping_address", models.CharField(max_length=50)),
                ("shipping_zip_code", models.CharField(max_length=10)),
                ("shipping_city", models.CharField(max_length=50)),
                ("shipping_province", models.CharField(max_length=5)),
                ("shipping_state", models.CharField(max_length=20)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="customer",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="customer",
            name="is_premium",
            field=models.BooleanField(default=False),
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
                        to="shop10.customer",
                    ),
                ),
            ],
        ),
        migrations.RunPython(
            code=forward_func_0004,
            reverse_code=backward_func_0004,
        ),
        migrations.RemoveField(
            model_name="customer",
            name="shipping_state",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="shipping_province",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="shipping_city",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="shipping_zip_code",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="shipping_address",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="shipping_name",
        ),
        migrations.AlterField(
            model_name="shippingaddress",
            name="address",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="shippingaddress",
            name="city",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="shippingaddress",
            name="name",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="shippingaddress",
            name="state",
            field=models.CharField(max_length=50),
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
        migrations.AddField(
            model_name="order",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
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
                ("product_quantity", models.FloatField()),
                ("product_unit_price", models.FloatField()),
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
        migrations.AlterField(
            model_name="customer",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="shop10_customer",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="customer",
            name="customer_type",
            field=models.IntegerField(choices=[(0, "Free"), (1, "Premium")], default=0),
        ),
        migrations.RunPython(
            code=forward_func_0017,
            reverse_code=backward_func_0017,
        ),
        migrations.RemoveField(
            model_name="customer",
            name="is_premium",
        ),
        migrations.AlterField(
            model_name="customer",
            name="customer_type",
            field=models.IntegerField(
                choices=[(0, "Free"), (1, "Premium"), (2, "Bronze")], default=0
            ),
        ),
        migrations.AlterField(
            model_name="customer",
            name="customer_type",
            field=models.IntegerField(
                choices=[(0, "Free"), (1, "Premium"), (2, "Bronze"), (3, "Silver")],
                default=0,
            ),
        ),
        migrations.AlterField(
            model_name="customer",
            name="customer_type",
            field=models.IntegerField(
                choices=[
                    (0, "Free"),
                    (1, "Premium"),
                    (2, "Bronze"),
                    (3, "Silver"),
                    (4, "Gold"),
                ],
                default=0,
            ),
        ),
        migrations.AlterField(
            model_name="customer",
            name="customer_type",
            field=models.IntegerField(
                choices=[
                    (0, "Free"),
                    (1, "Premium"),
                    (2, "Bronze"),
                    (3, "Silver"),
                    (4, "Gold"),
                    (5, "Platinum"),
                ],
                default=0,
            ),
        ),
        migrations.AlterField(
            model_name="customer",
            name="customer_type",
            field=models.IntegerField(
                choices=[
                    (0, "Free"),
                    (1, "Premium"),
                    (2, "Bronze"),
                    (3, "Silver"),
                    (4, "Gold"),
                    (5, "Platinum"),
                    (6, "Diamond"),
                ],
                default=0,
            ),
        ),
        migrations.AlterField(
            model_name="customer",
            name="customer_type",
            field=models.IntegerField(
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
        migrations.RenameField(
            model_name="orderline",
            old_name="product_quantity",
            new_name="quantity",
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
    ]
