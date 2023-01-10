from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.utils import IntegrityError
from django.test import TestCase

from shop04.models import Customer, OrderLine, Product, ShippingAddress


class ShopTestCase(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        self.u1 = UserModel.objects.create(username="foo")
        self.u2 = UserModel.objects.create(username="bar")
        self.c2 = Customer.objects.create(user=self.u2)

    def test_customer_uniqueness_with_user(self):
        Customer.objects.create(user=self.u1, customer_type=Customer.CustomerType.FREE)
        with self.assertRaises(Exception) as raised:
            with transaction.atomic():
                Customer.objects.create(
                    user=self.u1,
                    customer_type=Customer.CustomerType.PREMIUM,
                )
        self.assertEqual(IntegrityError, type(raised.exception))
        self.u1.refresh_from_db()
        self.assertEqual(
            self.u1.shop04_customer.customer_type, Customer.CustomerType.FREE
        )

    def test_customer_type_default_false(self):
        customer = Customer.objects.create(
            user=self.u1,
        )
        self.assertEqual(customer.customer_type, Customer.CustomerType.FREE)

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

    def test_order_amounts(self):
        order = self.c2.orders.create()
        order.lines.create(
            product_name="product",
            product_um="Unit(s)",
            product_unit_price=3.4,
            quantity=12,
        )
        self.assertEqual(
            order.lines.first().amount,
            3.4 * 12,
        )
        order.lines.create(
            product_name="product",
            product_um="Unit(s)",
            product_unit_price=7.8,
            quantity=56,
        )
        self.assertEqual(
            order.total_amount,
            (3.4 * 12) + (7.8 * 56),
        )

    def test_customer_products(self):
        customer = Customer.objects.create(
            user=self.u1,
        )
        customer.full_clean()
        product = customer.products.create(
            name="product",
            um="unit",
            unit_price=1.23,
        )
        product.full_clean()

    def test_order_copy_product(self):
        product = self.c2.products.create(
            name="1" * Product.name.field.max_length,
            um="1" * Product.um.field.max_length,
            unit_price=1.23,
        )
        product.full_clean()
        order = self.c2.orders.create()
        line = OrderLine(
            order=order,
            quantity=5,
        )
        line.copy_product(product)
        line.full_clean()
        line.save()
