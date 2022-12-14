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
        Customer.objects.create(
            user=self.u1,
            shipping_name="1",
            shipping_address="1",
            shipping_zip_code="1",
            shipping_city="1",
            shipping_province="1",
            shipping_state="1",
        )
        with self.assertRaises(Exception) as raised:
            with transaction.atomic():
                Customer.objects.create(
                    user=self.u1,
                    shipping_name="2",
                    shipping_address="2",
                    shipping_zip_code="2",
                    shipping_city="2",
                    shipping_province="2",
                    shipping_state="2",
                )
        self.assertEqual(IntegrityError, type(raised.exception))
        self.u1.refresh_from_db()
        self.assertEqual(self.u1.customer.shipping_name, "1")

    def test_customer_is_premium_default_false(self):
        customer = Customer.objects.create(
            user=self.u1,
            shipping_name="1",
            shipping_address="1",
            shipping_zip_code="1",
            shipping_city="1",
            shipping_province="1",
            shipping_state="1",
        )
        self.assertFalse(customer.is_premium)
