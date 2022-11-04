# Importing the logic from the logic file
from logic.logic_func import *

# Function that will be passed to the main file
def user_interface():
    # Printing the table initially
    print_table()
    
    
    is_running = True # Setting the program to running initially
    while is_running: # Programme running loops
        # Displaying the user their options
        print("\nSelect one of the following options")
        print("1. Enter book\n2. Update book\n3. Delete book\n4. Search book\n5. View all books\n0. Exit")
        # Logic for user input
        while True:
            try:
                user_choice = int(input("Enter: "))
                if user_choice >= 0  and user_choice < 6:
                    break
                print("Enter a valid choice 1 to 5")
            except ValueError:
                print("Enter a valid choice 1 to 5")

        # If statements used to run the required functions in logic file
        # No need for else because user input is already handled
        if user_choice == 1:
            add_book()
        elif user_choice == 2:
            update_info()
        elif user_choice == 3:
            delete_book()   
        elif user_choice == 4:
            search_book()
        elif user_choice == 5:
            print_table()
        elif user_choice == 0:
            is_running = False
        
        # Committing changes to database
        db.commit()


