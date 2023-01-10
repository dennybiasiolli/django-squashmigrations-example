# Generated by Django 4.1.4 on 2022-12-15 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop09", "0023_alter_customer_customer_type"),
    ]

    operations = [
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
    ]
