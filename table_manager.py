from datetime import datetime

from main import Menu, ReservationManager
from table import Table


class TableManager:
    def __init__(self):
        self.tables = {i: Table(i, (i % 2 + 4))for i in range(1, 11)}  # Default 10 tables

    def add_table(self, table_number, number_of_seats):
        self.tables[table_number] = Table(table_number, number_of_seats)

    def update_table(self, table_number, new_number_of_seats):
        if table_number in self.tables:
            self.tables[table_number].number_of_seats = new_number_of_seats

    def delete_table(self, table_number):
        if table_number in self.tables:
            del self.tables[table_number]

    def print_tables(self):
        for table in self.tables.values():
            print(table)

# Future date available
def is_future_date(date_str, time_str):
    """Check if the given date and time are in the future."""
    input_datetime = datetime.strptime(
        f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
    current_datetime = datetime.now()
    return input_datetime > current_datetime

# Implementing Staff Functions
def staff_options(menu, reservation_manager, table_manager):
    while True:
        print("\nStaff Options:")
        print("1. View Restaurant Details")
        print("2. Manage Menu")
        print("3. Manage Reservations")
        print("4. Manage Tables")
        print("5. Back to Main Menu")
        staff_choice = input("Enter your choice: ")

        if staff_choice == "1":
            view_restaurant_details()
        elif staff_choice == "2":
            manage_menu(menu)
        elif staff_choice == "3":
            manage_reservations(reservation_manager)
        elif staff_choice == "4":
            manage_tables(table_manager)
        elif staff_choice == "5":
            break

# Restaurant Details Function
def view_restaurant_details():
    print("Restaurant Details")
    print("Name: PDP Restaurant")
    print("Address: Sergeli district, Yangi Sergeli street, 12, Tashkent 100022, Tashkent")
    print("Phone: 998 78 777 7747")
    print("Website: www.university.pdp.uz")
    print("Opening Hours: 7 AM - 11 PM")

# Manage Menu Function
def manage_menu(menu):
    while True:
        print("\nMenu Management")
        print("1. Add new food")
        print("2. Update an order")
        print("3. Delete an order")
        print("4. View menu")
        print("5. Back to main menu")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter the name of the new food: ")
            price = float(input("Enter the price: "))
            description = input("Enter a description: ")
            menu.add_item(name, price, description)
            print("Food added successfully.")

        elif choice == "2":
            name = input("Enter the name of the food to update: ")
            new_name = input("Enter the new name: ")
            new_price = float(input("Enter the new price: "))
            new_description = input("Enter the new description: ")
            menu.update_item(name, new_name, new_price, new_description)
            print("Item updated successfully.")

        elif choice == "3":
            name = input("Enter the name of the food to delete: ")
            menu.remove_item(name)
            print("Item deleted successfully.")

        elif choice == "4":
            menu.print_menu()

        elif choice == "5":
            break

# Manage Reservation Function
def manage_reservations(reservation_manager):
    while True:
        print("\nReservation Management")
        print("1. View all reservations")
        print("2. View a specific reservation")
        print("3. Cancel a reservation")
        print("4. Back to main menu")
        choice = input("Choose an option: ")

        if choice == "1":
            reservation_manager.print_all_reservations()

        elif choice == "2":
            try:
                reservation_id = int(input("Enter the reservation ID: "))
                reservation = reservation_manager.get_reservation(
                    reservation_id)
                if reservation:
                    reservation.print_reservation()
                else:
                    print("No reservation found.")
            except ValueError:
                print("Invalid input. Please enter a valid reservation ID.")


        elif choice == "3":
            try:
                reservation_id = int(
                    input("Enter the reservation ID to cancel: "))
                reservation_manager.cancel_reservation(reservation_id)
            except ValueError:
                print("Invalid input. Please enter a valid reservation ID.")

        elif choice == "4":
            break

# Implementing Customer Functions
def view_menu(menu):
    menu.print_menu()

# Make Reservation Function
def make_reservation(reservation_manager, menu, table_manager):
    name = input("Enter your name: ")
    while True:
        date = input("Enter reservation date (YYYY-MM-DD): ")
        time = input("Enter reservation time (HH:MM): ")
        if is_future_date(date, time):
            break
        else:
            print("Please enter a future date and time.")
    guests = int(input("Enter number of guests: "))

    print("\nAvailable Tables:")
    table_manager.print_tables()
    table_number = input("Enter table number: ")

    reservation_id = reservation_manager.create_reservation(
        name, date, time, guests, table_number)

    if reservation_id:
        print(f"\nReservation successful! Your reservation ID is: {reservation_id}")
        reservation = reservation_manager.get_reservation(reservation_id)
        print("Menu:")
        menu.print_menu()
        print("Select up to 10 meals. Enter 'done' to finish.")
        while True:
            meal_choice = input(
                "Enter meal name to add (or type 'end' to finish): ")
            meal_choice_lower = meal_choice.lower()
            found_meal = next(
                (key for key in menu.items if key.lower() == meal_choice_lower), None)

            if meal_choice == 'end':
                break
            if found_meal:
                reservation.add_meal(
                    found_meal, menu.items[found_meal]['price'])
            else:
                print("Food not found. Please try again.")

        print("\nHere's your reservation summary:")
        reservation.print_reservation()
    else:
        print("This seat is booked or invalid time/date provided.")

# View Reservation Function
def view_reservation_details(reservation_manager):
    try:
        reservation_id = int(input("Enter your reservation ID: "))
        reservation = reservation_manager.reservations.get(reservation_id)
        if reservation:
            reservation.print_reservation()
        else:
            print("No reservation found for this ID.")
    except ValueError:
        print("Invalid input. Please enter a valid reservation ID.")

# Cancel Reservation Function
def cancel_reservation(reservation_manager):
    try:
        reservation_id = int(input("Enter the reservation ID to cancel: "))
        reservation_manager.cancel_reservation(reservation_id)
    except ValueError:
        print("Invalid input. Please enter a valid reservation ID.")


# Update Reservation Function
def update_reservation_details(reservation_manager, menu):
    try:
        reservation_id = int(input("Enter your reservation ID: "))
        reservation = reservation_manager.get_reservation(reservation_id)
        if reservation:
            print("Current reservation details:")
            reservation.print_reservation()

            # Update number of guests
            new_guests = int(input(
                "Enter the new number of guests (or press Enter to keep current): ") or reservation.guests)
            reservation.update_guests(new_guests)

            # Update meals
            print("\nWould you like to update meals? (yes/no): ")
            if input().lower().startswith('y'):
                print("Current meals in reservation:")
                for meal, details in reservation.meals.items():
                    print(f"{meal} x {details['quantity']}")

                print("\nSelect an option:")
                print("1. Add a meal")
                print("2. Remove a meal")
                print("3. End")
                while True:
                    meal_choice = input("Choose an option: ")
                    if meal_choice == "1":
                        menu.print_menu()
                        meal_to_add = input("Enter meal name to add: ")
                        if menu.is_item_available(meal_to_add):
                            reservation.add_meal(
                                meal_to_add, menu.items[meal_to_add]['price'])
                        else:
                            print("Meal not found. Please try again.")
                    elif meal_choice == "2":
                        meal_to_remove = input("Enter meal name to remove: ")
                        reservation.remove_meal(meal_to_remove)
                    elif meal_choice == "3":
                        break

            print("\nReservation updated:")
            reservation.print_reservation()
        else:
            print("No reservation found with this ID.")
    except ValueError:
        print("Invalid input. Please enter a valid reservation ID.")

# Customer options function
def customer_options(menu, reservation_manager, table_manager):
    while True:
        print("\nCustomer Options:")
        print("1. View Menu")
        print("2. Make a Reservation")
        print("3. View Restaurant Details")
        print("4. Cancel a Reservation")
        print("5. View Reservation Details")
        print("6. Update Reservation Details")
        print("7. Back to Main Menu")
        customer_choice = input("Enter your choice: ")
        print('==========================')
        if customer_choice == "1":
            view_menu(menu)
        elif customer_choice == "2":
            make_reservation(reservation_manager, menu, table_manager)
        elif customer_choice == "3":
            view_restaurant_details()
        elif customer_choice == "4":
            cancel_reservation(reservation_manager)
        elif customer_choice == "5":
            view_reservation_details(reservation_manager)
        elif customer_choice == "6":
            update_reservation_details(
                reservation_manager, menu)  # Pass 'menu' here
        elif customer_choice == "7":
            break


# Manage Tables Function
def manage_tables(table_manager):
    while True:
        print("\nTable Management")
        print("1. Add new table")
        print("2. Update a table")
        print("3. Delete a table")
        print("4. View tables")
        print("5. Back to main menu")
        choice = input("Choose an option: ")

        if choice == "1":
            table_number = int(input("Enter the table number: "))
            number_of_seats = int(input("Enter the number of seats: "))
            table_manager.add_table(table_number, number_of_seats)
            print("Table added successfully.")

        elif choice == "2":
            table_number = int(input("Enter the table number to update: "))
            new_number_of_seats = int(input("Enter the new number of seats: "))
            table_manager.update_table(table_number, new_number_of_seats)
            print("Table updated successfully.")

        elif choice == "3":
            table_number = int(input("Enter the table number to delete: "))
            table_manager.delete_table(table_number)
            print("Table deleted successfully.")

        elif choice == "4":
            print("\nCurrent Tables:")
            table_manager.print_tables()

        elif choice == "5":
            break

# Main Program
def main():
    menu = Menu()
    reservation_manager = ReservationManager()
    table_manager = TableManager()


    while True:
        print("\nWelcome to our restaurant! Select your role:")
        print("1. Customer")
        print("2. Staff")
        print("3. Exit")
        choice = input("Enter your choice: ")
        print('==========================')

        if choice == "1":
            customer_options(menu, reservation_manager, table_manager)
        elif choice == "2":
            staff_options(menu, reservation_manager, table_manager)
        elif choice == "3":
            break


if __name__ == "__main__":
    main()