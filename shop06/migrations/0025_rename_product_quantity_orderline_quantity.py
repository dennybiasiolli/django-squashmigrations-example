# Generated by Django 4.1.4 on 2022-12-15 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop06", "0024_alter_customer_customer_type"),
    ]

    operations = [
        migrations.RenameField(
            model_name="orderline",
            old_name="product_quantity",
            new_name="quantity",
        ),
    ]
