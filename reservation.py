class Reservation:
    def __init__(self, name, date, time, guests, table_number):
        self.name = name
        self.date = date
        self.time = time
        self.guests = guests
        self.table_number = table_number
        self.meals = {}
        self.total = 0

    def add_meal(self, meal_name, price):
        if meal_name in self.meals:
            self.meals[meal_name]['quantity'] += 1
        else:
            self.meals[meal_name] = {'price': price, 'quantity': 1}
        self.total += price

    def remove_meal(self, meal_name):
        if meal_name in self.meals:
            self.total -= self.meals[meal_name]['price'] * \
                self.meals[meal_name]['quantity']
            del self.meals[meal_name]

    def calculate_total(self):
        self.total = sum(item['price'] * item['quantity'] for item in self.meals.values())
        return self.total

    def update_guests(self, number_of_guests):
        self.guests = number_of_guests

    def print_reservation(self):
        print(f"Reservation for {self.name} on {self.date} at {self.time} for {self.guests} guests at table {self.table_number}.")
        for meal, details in self.meals.items():
            print(f"{meal} x {details['quantity']}: ${details['price'] * details['quantity']}")
        print(f"Total Cost: ${self.calculate_total()}")