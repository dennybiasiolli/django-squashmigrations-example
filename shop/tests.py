from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.utils import IntegrityError
from django.test import TestCase

from shop.models import Customer, ShippingAddress


class ShopTestCase(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        self.u1 = UserModel.objects.create(username="foo")
        self.u2 = UserModel.objects.create(username="bar")
        self.c2 = Customer.objects.create(user=self.u2)

    def test_customer_uniqueness_with_user(self):
        Customer.objects.create(user=self.u1, is_premium=False)
        with self.assertRaises(Exception) as raised:
            with transaction.atomic():
                Customer.objects.create(user=self.u1, is_premium=True)
        self.assertEqual(IntegrityError, type(raised.exception))
        self.u1.refresh_from_db()
        self.assertFalse(self.u1.customer.is_premium, "1")

    def test_customer_is_premium_default_false(self):
        customer = Customer.objects.create(
            user=self.u1,
        )
        self.assertFalse(customer.is_premium)

    def test_customer_shipping_addresses(self):
        customer = Customer.objects.create(
            user=self.u1,
        )
        customer.full_clean()
        shipping_address = customer.shipping_addresses.create(
            name="1",
            address="1",
            zip_code="1",
            city="1",
            province="1",
            state="1",
        )
        shipping_address.full_clean()

    def test_order_copy_shipping_address(self):
        shipping_address = self.c2.shipping_addresses.create(
            name="1" * ShippingAddress.name.field.max_length,
            address="1" * ShippingAddress.address.field.max_length,
            zip_code="1" * ShippingAddress.zip_code.field.max_length,
            city="1" * ShippingAddress.city.field.max_length,
            province="1" * ShippingAddress.province.field.max_length,
            state="1" * ShippingAddress.state.field.max_length,
        )
        order = self.c2.orders.create()
        order.full_clean()
        order.copy_shipping_address(shipping_address)
        order.full_clean()
        order.save()
