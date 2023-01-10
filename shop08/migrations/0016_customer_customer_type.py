# Generated by Django 4.1.4 on 2022-12-15 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop08", "0015_alter_customer_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="customer_type",
            field=models.IntegerField(choices=[(0, "Free"), (1, "Premium")], default=0),
        ),
    ]
