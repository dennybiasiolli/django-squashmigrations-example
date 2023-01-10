# Generated by Django 4.1.4 on 2022-12-15 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop13", "0019_alter_customer_customer_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="customer_type",
            field=models.IntegerField(
                choices=[(0, "Free"), (1, "Premium"), (2, "Bronze"), (3, "Silver")],
                default=0,
            ),
        ),
    ]
