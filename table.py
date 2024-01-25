class Table:
    def __init__(self, table_number, number_of_seats):
        self.table_number = table_number
        self.number_of_seats = number_of_seats

    def __str__(self):
        return f"Table {self.table_number}, Seats: {self.number_of_seats}"