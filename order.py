class OrderItem:
    def __init__(self, menu_item, quantity):
        self.menu_item = menu_item
        if quantity <= 0:
            raise ValueError("Order item quantity must be greater than zero.")
        self.quantity = quantity

    def get_subtotal(self):
        return self.menu_item.get_price() * self.quantity


class Order:
    def __init__(self, order_id, order_date, customer_name, restaurant, rider):
        self.order_id = order_id
        self.order_date = order_date
        self.customer_name = customer_name
        self.restaurant = restaurant
        self.rider = rider
        self.items = []

    def add_item(self, order_item):
        self.items.append(order_item)

    def calculate_total(self):
        total = 0.0
        for item in self.items:
            total += item.get_subtotal()
        return total
