# Generated by Django 4.1.4 on 2022-12-14 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop08", "0008_remove_customer_shipping_zip_code"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customer",
            name="shipping_address",
        ),
    ]