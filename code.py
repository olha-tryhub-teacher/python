class OrderItem: #### new
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def calculate_subtotal(self):
        return self.product.price * self.quantity

class OrderProcessor: #### new
    def process_order(self, order, discount_strategy):
        total = order.calculate_total()
        total_after_discount = discount_strategy.apply_discount(total)
        if total_after_discount > 100:
            order.status = "Completed"

# Використання
customer = Customer("John")
product1 = Product("Laptop", 1000)
product2 = Product("Headphones", 100)
order = Order(customer)
order.add_item(product1, 2)
order.add_item(product2, 1)

discount_strategy = FixedDiscount(50)
order_processor = OrderProcessor()
order_processor.process_order(order, discount_strategy)

print(f"Order total: ${order.calculate_total()}")
print(f"Order status: {order.status}")
