# Generated by Django 4.1.4 on 2022-12-14 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop20", "0009_remove_customer_shipping_address"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customer",
            name="shipping_name",
        ),
    ]
