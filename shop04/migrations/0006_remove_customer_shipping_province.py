# Generated by Django 4.1.4 on 2022-12-14 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop04", "0005_remove_customer_shipping_state"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customer",
            name="shipping_province",
        ),
    ]
