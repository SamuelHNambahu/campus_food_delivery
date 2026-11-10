import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from employee import DeliveryRider, RestaurantStaff
from restaurant import Restaurant, MenuItem
from order import OrderItem
from platform_system import Platform


platform = Platform("CampusEats")

grill_house = Restaurant(1, "Grill House", "Independence Avenue, Windhoek")
noodle_bar = Restaurant(2, "Noodle Bar", "Klein Windhoek")
platform.add_restaurant(grill_house)
platform.add_restaurant(noodle_bar)

burger = MenuItem(101, "Beef Burger", 55.0)
chips = MenuItem(102, "Chips", 20.0)
grill_house.add_menu_item(burger)
grill_house.add_menu_item(chips)

noodles = MenuItem(201, "Stir-fry Noodles", 48.0)
noodle_bar.add_menu_item(noodles)

pizza_place = Restaurant(3, "Pizza Place", "Eros, Windhoek")
platform.add_restaurant(pizza_place)

rider_bike = DeliveryRider(1, "Johan", "0811234567", "bicycle", 5.0)
rider_car = DeliveryRider(2, "Mariam", "0817654321", "car", 12.0)
platform.add_rider(rider_bike)
platform.add_rider(rider_car)

staff_member = RestaurantStaff(3, "Petrus", "0819876543", 8.0, 35.0)

window = tk.Tk()
window.title("Campus Food Delivery System")
window.geometry("850x520")

def show_output(text):
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, text)

def view_menu():
    text = ""
    for restaurant in platform.restaurants:
        text += f"{restaurant.name}\n"
        for item in restaurant.get_menu():
            text += f"  {item.name} - N$ {item.get_price():.2f}\n"
        text += "\n"
    show_output(text)

def show_summary():
    show_output(platform.generate_daily_summary())

def open_order_window():
    popup = tk.Toplevel(window)
    popup.title("Place Order")
    popup.geometry("950x330")

    choices = []
    for restaurant in platform.restaurants:
        for item in restaurant.get_menu():
            choices.append(f"{restaurant.name} - {item.name}")

    rider_names = []
    for rider in platform.riders:
        rider_names.append(rider.get_name())

    tk.Label(popup, text="Customer name").pack(pady=2)
    name_entry = tk.Entry(popup)
    name_entry.pack()

    tk.Label(popup, text="Item").pack(pady=2)
    item_box = ttk.Combobox(popup, values=choices, state="readonly")
    item_box.pack()

    tk.Label(popup, text="Quantity").pack(pady=2)
    quantity_entry = tk.Entry(popup)
    quantity_entry.pack()

    tk.Label(popup, text="Rider").pack(pady=2)
    rider_box = ttk.Combobox(popup, values=rider_names, state="readonly")
    rider_box.pack()

    def submit_order():
        try:
            quantity = int(quantity_entry.get())
            selected_restaurant = None
            selected_item = None
            for restaurant in platform.restaurants:
                for item in restaurant.get_menu():
                    if f"{restaurant.name} - {item.name}" == item_box.get():
                        selected_restaurant = restaurant
                        selected_item = item
            selected_rider = None
            for rider in platform.riders:
                if rider.get_name() == rider_box.get():
                    selected_rider = rider
            if name_entry.get() == "" or selected_item is None or selected_rider is None:
                raise ValueError("Please fill in all fields.")
            order_item = OrderItem(selected_item, quantity)
            order_id = 1001 + len(platform.orders)
            order = platform.place_order(order_id, "2026-09-09", name_entry.get(), selected_restaurant, selected_rider)
            order.add_item(order_item)
            messagebox.showinfo("Order placed", f"Order {order_id} total: N$ {order.calculate_total():.2f}")
            popup.destroy()
        except ValueError as e:
            messagebox.showerror("Invalid input", str(e))

    tk.Button(popup, text="Place Order", command=submit_order).pack(pady=15)

def process_order():
    try:
        show_output(platform.process_next_order())
    except IndexError as e:
        messagebox.showerror("Queue empty", str(e))

def save_report():
    show_output(platform.save_report_to_file("daily_report.txt"))

def load_menu():
    try:
        pizza_place.load_menu_from_file("menu.txt")
        show_output(f"Menu loaded. Pizza Place now has {len(pizza_place.get_menu())} items.")
    except FileNotFoundError as e:
        messagebox.showerror("File not found", str(e))

def show_polymorphism():
    text = "1. Overriding - calculate_daily_wage()\n"
    for employee in [rider_bike, rider_car, staff_member]:
        text += f"  {employee.get_name()}: N$ {employee.calculate_daily_wage():.2f}\n"

    text += "\n2. Duck typing - generate_report()\n"
    for obj in [grill_house, platform]:
        text += f"  {obj.generate_report()}\n"

    text += "\n3. Overloading style - apply_discount()\n"
    text += f"  Default discount: N$ {burger.apply_discount():.2f}\n"
    text += f"  25% discount: N$ {burger.apply_discount(25):.2f}\n"
    show_output(text)

def eco_bonus():
    text = platform.apply_eco_bonus(rider_bike) + "\n"
    text += platform.apply_eco_bonus(rider_car)
    show_output(text)

button_frame = tk.Frame(window)
button_frame.pack(side="left", padx=10, pady=10)

output_box = tk.Text(window, height=25, width=60, wrap="word")
output_box.pack(side="right", padx=10, pady=10)

menu_button = tk.Button(button_frame, text="View Menu", command=view_menu)
menu_button.pack(pady=5)

summary_button = tk.Button(button_frame, text="Daily Summary", command=show_summary)
summary_button.pack(pady=5)

order_button = tk.Button(button_frame, text="Place Order", command=open_order_window)
order_button.pack(pady=5)

process_button = tk.Button(button_frame, text="Process Next Order", command=process_order)
process_button.pack(pady=5)

save_button = tk.Button(button_frame, text="Save Report to File", command=save_report)
save_button.pack(pady=5)

load_button = tk.Button(button_frame, text="Load Pizza Place Menu", command=load_menu)
load_button.pack(pady=5)

poly_button = tk.Button(button_frame, text="Polymorphism Demo", command=show_polymorphism)
poly_button.pack(pady=5)

eco_button = tk.Button(button_frame, text="Eco Bonus Check", command=eco_bonus)
eco_button.pack(pady=5)

menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Save Report", command=save_report)
file_menu.add_command(label="Exit", command=window.destroy)
menu_bar.add_cascade(label="File", menu=file_menu)

view_options = tk.Menu(menu_bar, tearoff=0)
view_options.add_command(label="Restaurant Menus", command=view_menu)
view_options.add_command(label="Daily Summary", command=show_summary)
menu_bar.add_cascade(label="View", menu=view_options)

window.mainloop()