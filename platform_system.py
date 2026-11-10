from employee import DeliveryRider
from order import Order
from order_queue import OrderQueue

class Platform:
    def __init__(self, platform_name):
        self.platform_name = platform_name
        self.orders = []
        self.restaurants = []
        self.riders = []
        self.pending_orders = OrderQueue()

    def generate_report(self):
        return f"Platform Report — {self.platform_name}: {len(self.orders)} total orders, {len(self.restaurants)} restaurants"

    def add_restaurant(self, restaurant):
        self.restaurants.append(restaurant)

    def add_rider(self, rider):
        self.riders.append(rider)

    def place_order(self, order_id, order_date, customer_name, restaurant, rider):
        order = Order(order_id, order_date, customer_name, restaurant, rider)
        self.orders.append(order)
        restaurant.record_order(order)
        self.pending_orders.enqueue(order)
        return order

    def calculate_average_order_value(self):
        if len(self.orders) == 0:
            return 0.0
        total = 0.0
        for order in self.orders:
            total += order.calculate_total()
        return total / len(self.orders)

    def apply_eco_bonus(self, rider):
        if not isinstance(rider, DeliveryRider):
            raise ValueError("Eco bonus can only be applied to a DeliveryRider.")
        if rider.vehicle_type == "bicycle":
            rider.record_delivery()
            return f"Eco bonus applied to {rider.get_name()} (bicycle rider)."
        return f"{rider.get_name()} does not qualify for the eco bonus (uses {rider.vehicle_type})."

    def find_top_restaurant(self):
        if len(self.restaurants) == 0:
            return None
        top_restaurant = self.restaurants[0]
        for restaurant in self.restaurants:
            if restaurant.get_total_revenue() > top_restaurant.get_total_revenue():
                top_restaurant = restaurant
        return top_restaurant

    def generate_daily_summary(self):
        total_orders = len(self.orders)
        total_revenue = 0.0
        for order in self.orders:
            total_revenue += order.calculate_total()
        average_value = self.calculate_average_order_value()

        summary = (f"Daily Summary for {self.platform_name}\n" f"Total orders: {total_orders}\n" f"Total revenue: N$ {total_revenue:.2f}\n" f"Average order value: N$ {average_value:.2f}")
        return summary

    def process_next_order(self):
        if self.pending_orders.is_empty():
            raise IndexError("No pending orders to process.")
        order = self.pending_orders.dequeue()
        return f"Processing order {order.order_id} for {order.customer_name} (N$ {order.calculate_total():.2f})"

    def save_report_to_file(self, filename):
        report = self.generate_daily_summary()
        with open(filename, "w") as file:
            file.write(report)
        return f"Report saved to {filename}"