from нава модуля import *

import unittest



# Ваш код класів і функцій тут (залишено незмінним)

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("John")
        self.product1 = Product("Laptop", 1000)
        self.product2 = Product("Headphones", 100)
        self.order = Order(self.customer)
        self.order.add_item(self.product1, 2)
        self.order.add_item(self.product2, 1)

    def test_calculate_total(self):
        total = self.order.calculate_total()
        self.assertEqual(total, 2100)

    def test_order_status_processing(self):
        self.assertEqual(self.order.status, "Processing")

    def test_order_status_completed(self):
        discount_strategy = FixedDiscount(50)
        order_processor = OrderProcessor()
        order_processor.process_order(self.order, discount_strategy)
        self.assertEqual(self.order.status, "Completed")

    def test_order_status_not_completed(self):
        discount_strategy = FixedDiscount(10)
        order_processor = OrderProcessor()
        order_processor.process_order(self.order, discount_strategy)
        self.assertEqual(self.order.status, "Processing")


if __name__ == "__main__":
    unittest.main()
