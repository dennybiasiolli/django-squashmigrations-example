# Generated by Django 4.1.4 on 2022-12-14 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop18", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="is_premium",
            field=models.BooleanField(default=False),
        ),
    ]
