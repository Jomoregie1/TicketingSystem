from baseuser import BaseUser
import copy


class User(BaseUser):
    all_users = {}

    def __init__(self):
        self.username = None
        self.theatre = self.get_theatre()
        self.purchased_tickets = []
        self.login_attempts = 0

        while True:
            try:
                answer = input("Are you a new user? (Y/N) ").lower()
                print("\n")
                if answer == "y":
                    self.register()
                    break
                elif answer == "n":
                    username = input("Enter username here: ").lower()
                    self.login(username)
                    break
                else:
                    raise ValueError()
            except ValueError:
                print("Invalid input provided, please try again")

        self.display_menu()

    def register(self):
        isNotUnique = True
        print("----------- Register -------------")
        while isNotUnique:
            self.username = input("Enter a new username here:  ").lower()
            if self.username not in User.all_users.keys():
                User.all_users[self.username] = self
                isNotUnique = False
            else:
                print("Please try a again")

    def login(self, username):

        notLoggedIn = True

        while self.login_attempts <= 3 and notLoggedIn:
            if username in User.all_users.keys():
                print(f"User: {username} has successfully logged in.")

                logged_in_user = User.all_users[username]
                self.username = logged_in_user.username
                self.purchased_tickets = logged_in_user.purchased_tickets
                notLoggedIn = False
            else:
                print("Log-in attempt failed ")
                username = input("Enter a new username here:  ").lower()
                self.login_attempts += 1

        if self.login_attempts == 3:
            print("You failed your attempts to log in. Please register as a new user below.")
            self.login_attempts = 0
            self.register()

    def display_menu(self):

        while True:

            print("------------ Menu --------------")
            print("1. Book ticket\n2. Cancel ticket\n3. Show ticket\n4. Quit\n")
            choice = int(input("-> "))
            if choice == 1:
                self.book()
            elif choice == 2:
                self.cancel_ticket()
            elif choice == 3:
                self.show_tickets()
            elif choice == 4:
                break

    def book(self):

        self.theatre.display_seats(self.theatre.rows)
        isNotValidated = True

        while isNotValidated:
            row = int(input("Please enter the row: ")) - 1
            seat = int(input("Please enter the seat number: ")) - 1

            if self.theatre.validate_seat(row, seat):
                isNotValidated = False
                price = self.theatre.get_seat_price(row + 1)
                print(f"The price of the seat is: {price}")
                confirmation = input("Please confirm if you want the seat? (Y/N) ").lower()
                self.theatre.confirm_seat(row, seat, confirmation)
                self.purchased_tickets.append({"Row": row + 1,
                                               "Seat": seat + 1,
                                               "Price": price})

    def cancel_ticket(self):
        seating = copy.deepcopy(self.theatre.rows)
        for booking in self.purchased_tickets:
            seating[booking["Row"] - 1][booking["Seat"] - 1] = "B"
        self.theatre.display_seats(seating)
        seat_to_cancel = int(input("Please select a seat to cancel: "))
        row_to_cancel = int(input("Please select a row to cancel: "))
        ticket_to_remove = None
        isCancelled = False

        for i in range(len(self.purchased_tickets)):
            if seat_to_cancel == self.purchased_tickets[i]["Seat"] and row_to_cancel == self.purchased_tickets[i]["Row"]:
                print(f"Row: {self.purchased_tickets[i]['Row']}")
                print(f"Seat: {self.purchased_tickets[i]['Seat']}")
                print(f"Price: {self.purchased_tickets[i]['Price']}")

                isCancelled = input("Do you want to cancel? (Y/N)").lower()
                self.theatre.cancelTickets(row_to_cancel - 1, seat_to_cancel - 1, isCancelled)
                ticket_to_remove = i
                isCancelled = True

        if isCancelled:
            self.purchased_tickets.pop(ticket_to_remove)

    def show_tickets(self):
        for i in range(len(self.purchased_tickets)):
            print(f"Ticket {i + 1}")
            print(f"Row: {self.purchased_tickets[i]['Row']}")
            print(f"Seat: {self.purchased_tickets[i]['Seat']}")
            print(f"Price: {self.purchased_tickets[i]['Price']}")
            print("__________________________")
