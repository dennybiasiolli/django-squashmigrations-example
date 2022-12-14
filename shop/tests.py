from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.utils import IntegrityError
from django.test import TestCase

from shop.models import Customer


class ShopTestCase(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        self.u1 = UserModel.objects.create(username="foo")
        self.u2 = UserModel.objects.create(username="bar")

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
