# Generated by Django 4.1.4 on 2022-12-15 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shop11", "0013_order_created_at"),
    ]

    operations = [
        migrations.CreateModel(
            name="OrderLine",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("product_name", models.CharField(max_length=100)),
                ("product_um", models.CharField(max_length=10)),
                ("product_quantity", models.FloatField()),
                ("product_unit_price", models.FloatField()),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lines",
                        to="shop11.order",
                    ),
                ),
            ],
        ),
    ]
