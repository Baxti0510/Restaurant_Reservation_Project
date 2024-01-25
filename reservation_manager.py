import itertools

from main import Reservation


class ReservationManager:
    def __init__(self):
        self.reservations = {}
        self.id_counter = itertools.count(1)

    def is_available(self, date, time, table_number):
        for reservation_id, reservation in self.reservations.items():
            if reservation.date == date and reservation.time == time and reservation.table_number == table_number:
                return False
        return True

    def get_reservation(self, reservation_id):
        return self.reservations.get(reservation_id)

    def create_reservation(self, name, date, time, guests, table_number):
        if self.is_available(date, time, table_number):
            reservation_id = next(self.id_counter)  # Generate unique ID
            reservation = Reservation(name, date, time, guests, table_number)
            self.reservations[reservation_id] = reservation  # Use ID as key
            return reservation_id  # Return the new ID
        else:
            return False

    def print_all_reservations(self):
        if not self.reservations:
            print(f"No reservations found named : {self.name}.")
            return
        for reservation_id, reservation in self.reservations.items():
            print(f"Reservation ID: {reservation_id}")
            reservation.print_reservation()

    def cancel_reservation(self, reservation_id):
        if reservation_id in self.reservations:
            del self.reservations[reservation_id]
            print(f"Reservation {reservation_id} has been cancelled.")
        else:
            print("No reservation found with that ID.")