# Generated by Django 4.1.4 on 2022-12-14 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop02", "0007_remove_customer_shipping_city"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customer",
            name="shipping_zip_code",
        ),
    ]
