from user import User
from admin import Admin

while True:
    type_of_user = input("Are you an Admin or User?(Admin/User) ").lower()
    if type_of_user == "admin":
        Admin()
        if Admin.isTerminated:
            Admin.isTerminated = False
            break
    elif type_of_user == "user":
        User()
    else:
        print("Try again, Invalid input")
