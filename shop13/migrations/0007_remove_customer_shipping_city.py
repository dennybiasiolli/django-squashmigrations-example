# Generated by Django 4.1.4 on 2022-12-14 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop13", "0006_remove_customer_shipping_province"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customer",
            name="shipping_city",
        ),
    ]
