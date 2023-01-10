# Generated by Django 4.1.4 on 2022-12-15 09:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("shop13", "0014_orderline"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="shop13_customer",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
