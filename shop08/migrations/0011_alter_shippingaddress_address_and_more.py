# Generated by Django 4.1.4 on 2022-12-14 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop08", "0010_remove_customer_shipping_name"),
    ]

    operations = [
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
    ]
