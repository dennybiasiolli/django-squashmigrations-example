# Generated by Django 4.1.4 on 2022-12-14 19:59

from django.db import migrations


def forward_func(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    CustomerModel = apps.get_model("shop07", "Customer")
    customers = CustomerModel.objects.using(db_alias).all()
    for customer in customers:
        customer.shipping_addresses.create(
            name=customer.shipping_name,
            address=customer.shipping_address,
            zip_code=customer.shipping_zip_code,
            city=customer.shipping_city,
            province=customer.shipping_province,
            state=customer.shipping_state,
        )


def backward_func(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    CustomerModel = apps.get_model("shop07", "Customer")
    customers = CustomerModel.objects.using(db_alias).all()
    for customer in customers:
        shipping_address = customer.shipping_addresses.last()
        if shipping_address:
            customer.shipping_name = shipping_address.name
            customer.shipping_address = shipping_address.address
            customer.shipping_zip_code = shipping_address.zip_code
            customer.shipping_city = shipping_address.city
            customer.shipping_province = shipping_address.province
            customer.shipping_state = shipping_address.state
            customer.save()


class Migration(migrations.Migration):

    dependencies = [
        ("shop07", "0003_shippingaddress"),
    ]

    operations = [migrations.RunPython(forward_func, backward_func)]
