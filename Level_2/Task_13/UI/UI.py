from logic.logic_func import *


def user_interface():
    print_table()
    print("Select one of the following options")
    print("1. Enter book\n2. Update book\n3. Delete book\n4. Search book\n0. Exit")
    user_choice = int(input("Enter: "))
    add_book()


