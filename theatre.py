class Theatre:
    _instance = None

    def __new__(cls, prices=None, rows=None):
        if cls._instance is None:
            cls._instance = super(Theatre, cls).__new__(cls)
            cls._instance.prices = prices if prices else {
                1: 100, 2: 80, 3: 70, 4: 70, 5: 60, 6: 40, 7: 20
            }
            cls._instance.rows = rows if rows else cls.generate_seats(cls._instance)
        return cls._instance

    def display_seats(self, rows):
        final_seats_length = len(" ".join(rows[-1]))
        output_lines = [(" ".join(row)).center(final_seats_length) for row in reversed(rows)]
        for line in output_lines:
            print(line)

    def get_seat_price(self, row):
        return self.prices[row]

    def validate_seat(self, row, seat):
        try:
            if self.rows[row][seat] == "_":
                return True
            else:
                print("This seat has been sold, please select another seat!")

        except IndexError:
            print("Invalid row or seat number entered, please try again!")

        return False

    def confirm_seat(self, row, seat, confirmation):
        if confirmation == "y":
            self.rows[row][seat] = "x"

    def cancelTickets(self, row, seat, cancellation):
        if cancellation == "y":
            self.rows[row][seat] = "_"

    def generate_seats(self):
        return [["_"] * (8 + 2 * row) for row in range(7)]
