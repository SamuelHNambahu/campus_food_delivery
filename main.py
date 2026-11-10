from employee import DeliveryRider, RestaurantStaff
from restaurant import Restaurant, MenuItem
from order import OrderItem
from platform_system import Platform


def main():
    platform = Platform("CampusEats")

    grill_house = Restaurant(1, "Grill House", "Academia")
    noodle_bar = Restaurant(2, "Noodle Bar", "Khomasdal")
    platform.add_restaurant(grill_house)
    platform.add_restaurant(noodle_bar)

    burger = MenuItem(101, "Beef Burger", 55.0)
    chips = MenuItem(102, "Chips", 20.0)
    grill_house.add_menu_item(burger)
    grill_house.add_menu_item(chips)

    noodles = MenuItem(201, "Stir-fry Noodles", 48.0)
    spring_roll = MenuItem(202, "Spring Roll", 18.0)
    noodle_bar.add_menu_item(noodles)
    noodle_bar.add_menu_item(spring_roll)

    rider_bike = DeliveryRider(1, "Johan", "0811234567", "bicycle", 5.0)
    rider_car = DeliveryRider(2, "Mariam", "0817654321", "car", 12.0)
    staff_member = RestaurantStaff(3, "Petrus", "0819876543", 8.0, 35.0)
    platform.add_rider(rider_bike)
    platform.add_rider(rider_car)

    print("Testing polymorphism calculate_daily_wage()")
    for employee in [rider_bike, rider_car, staff_member]:
        print(f"{employee.get_name()}: N$ {employee.calculate_daily_wage():.2f}")
    print()

    print("Placing orders (composition Order composes OrderItems)")
    order1 = platform.place_order(1001, "2026-08-26", "Sammy", grill_house, rider_bike)
    order1.add_item(OrderItem(burger, 2))
    order1.add_item(OrderItem(chips, 1))
    print(f"Order {order1.order_id} total: N$ {order1.calculate_total():.2f}")

    order2 = platform.place_order(1002, "2026-08-26", "Ndeshi", noodle_bar, rider_car)
    order2.add_item(OrderItem(noodles, 3))
    print(f"Order {order2.order_id} total: N$ {order2.calculate_total():.2f}")
    print()

    try:
        OrderItem(burger, 0)
    except ValueError as e:
        print(f"Caught expected error: {e}")

    try:
        MenuItem(999, "Broken Item", -10.0)
    except ValueError as e:
        print(f"Caught expected error: {e}")
    print()

    print("Testing type-check method apply_eco_bonus()")
    print(platform.apply_eco_bonus(rider_bike))
    print(platform.apply_eco_bonus(rider_car))
    print()

    print("Testing basic algorithm (calculate_average_order_value())")
    print(f"Average order value: N$ {platform.calculate_average_order_value():.2f}")
    print()

    print("Testing basic algorithm find_top_restaurant()")
    top = platform.find_top_restaurant()
    print(f"Top restaurant: {top.name} (N$ {top.get_total_revenue():.2f} revenue)")
    print()

    print("Testing main-class method generate_daily_summary()")
    print(platform.generate_daily_summary())

    print("Testing Queue ADT (order processing)")
    print(platform.process_next_order())
    print(platform.process_next_order())
    print()

    print("Testing duck-typing polymorphism (generate_report())")
    reportable_objects = [grill_house, platform]
    for obj in reportable_objects:
        print(obj.generate_report())
    print()

    print("Testing overload-style polymorphism (apply_discount())")
    print(f"Burger with default discount: N$ {burger.apply_discount():.2f}")
    print(f"Burger with 25% discount: N$ {burger.apply_discount(25):.2f}")
    print()

    print("Testing save to file")
    print(platform.save_report_to_file("daily_report.txt"))
    print()

    print("Testing load from file")
    try:
        grill_house.load_menu_from_file("menu.txt")
        print(f"Menu loaded. Grill House now has {len(grill_house.get_menu())} items.")
    except FileNotFoundError as e:
        print(f"Caught expected error: {e}")


if __name__ == "__main__":
    main()
