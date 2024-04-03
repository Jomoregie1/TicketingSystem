from baseuser import BaseUser
from user import User


class Admin(BaseUser):
    isTerminated = False

    def __init__(self):
        self.theatre = self.get_theatre()
        self.display_menu()

    def display_menu(self):

        while True:
            print("------------ Menu --------------")
            print("1. View Ticketing Status \n2. Cancel ticket\n3. Reset\n4. Quit\n")
            choice = int(input("-> "))
            if choice == 1:
                self.view_ticketing_status()
            elif choice == 2:
                self.cancel_ticket()
            elif choice == 3:
                self.reset()
            elif choice == 4:
                Admin.isTerminated = True
                break

    def cancel_ticket(self):
        self.theatre.display_seats(self.theatre.rows)
        isNotValid = True

        while isNotValid:
            row = input("Please select a row to cancel: ")
            seat = input("Please select a seat to cancel: ")

            if self.theatre.rows[row][seat] == "x":
                price = self.theatre.get_seat_price(row, seat)
                print(f"Row: {row}\nSeat: {seat}\nPrice: {price}")
                confirmation = input("Do you want to cancel? (Y/N) ").lower()
                self.theatre.cancelTickets(row, seat, confirmation)
                isNotValid = False
            else:
                print("Please enter a valid seat number.")

    def view_ticketing_status(self):
        self.theatre.display_seats(self.theatre.rows)

    def reset(self):
        self.theatre.rows = self.theatre.generate_seats()
        for users in User.all_users.values():
            users.purchased_tickets.clear()
