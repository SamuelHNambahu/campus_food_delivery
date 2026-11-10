class Employee:

    def __init__(self, employee_id, name, phone_number):
        self.employee_id = employee_id
        self.name = name
        self.phone_number = phone_number

    def get_employee_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def get_phone_number(self):
        return self.phone_number
    
    def calculate_daily_wage(self):
        return 0.0


class DeliveryRider(Employee):
    def __init__(self, employee_id, name, phone_number, vehicle_type, delivery_radius_km):
        super().__init__(employee_id, name, phone_number)
        self.vehicle_type = vehicle_type
        self.delivery_radius_km = delivery_radius_km
        self.deliveries_completed = 0

    def get_vehicle_type(self):
        return self.vehicle_type

    def get_deliveries_completed(self):
        return self.deliveries_completed

    def record_delivery(self):
        self.deliveries_completed += 1

    def calculate_daily_wage(self):
        base_pay = 150.0
        bonus_per_delivery = 15.0
        return base_pay + (self.deliveries_completed * bonus_per_delivery)

    def calculate_delivery_time(self, distance_km):
        speeds = {"bicycle": 15.0, "scooter": 35.0, "car": 45.0}
        speed = speeds.get(self.vehicle_type, 25.0)
        hours = distance_km / speed
        return round(hours * 60, 1)


class RestaurantStaff(Employee):

    def __init__(self, employee_id, name, phone_number, shift_hours, hourly_rate):
        super().__init__(employee_id, name, phone_number)
        self.shift_hours = shift_hours
        self.hourly_rate = hourly_rate

    def calculate_daily_wage(self):
        return self.shift_hours * self.hourly_rate
