# Generated by Django 4.1.4 on 2022-12-15 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop16", "0018_remove_customer_is_premium"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="customer_type",
            field=models.IntegerField(
                choices=[(0, "Free"), (1, "Premium"), (2, "Bronze")], default=0
            ),
        ),
    ]
