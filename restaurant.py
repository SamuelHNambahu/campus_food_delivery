class MenuItem:
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        if price < 0:
            raise ValueError("Menu item price cannot be negative.")
        self.price = price

    def get_price(self):
        return self.price    

    def apply_discount(self, percentage=10):
        discount_amount = self.price * (percentage / 100)
        return self.price - discount_amount

class Restaurant:
    def __init__(self, restaurant_id, name, location):
        self.restaurant_id = restaurant_id
        self.name = name
        self.location = location
        self.menu_items = []
        self.received_orders = []

    def add_menu_item(self, item):
        if item.get_price() < 0:
            raise ValueError("Cannot add a menu item with a negative price.")
        self.menu_items.append(item)

    def get_menu(self):
        return self.menu_items

    def record_order(self, order):
        self.received_orders.append(order)

    def get_total_revenue(self):
        total = 0.0
        for order in self.received_orders:
            total += order.calculate_total()
        return total

    def generate_report(self):
        return f"Restaurant Report — {self.name}: {len(self.menu_items)} menu items, N$ {self.get_total_revenue():.2f} revenue"

    def load_menu_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                for line in file:
                    parts = line.strip().split(",")
                    item_id = int(parts[0])
                    name = parts[1]
                    price = float(parts[2])
                    self.add_menu_item(MenuItem(item_id, name, price))
        except FileNotFoundError:
            raise FileNotFoundError(f"Menu file '{filename}' was not found.")    