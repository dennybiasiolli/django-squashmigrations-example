# Generated by Django 4.1.4 on 2022-12-15 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop11", "0017_migrate_is_premium_to_customer_type"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customer",
            name="is_premium",
        ),
    ]
