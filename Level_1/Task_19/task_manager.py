#=====importing libraries===========
'''This is the section where you will import libraries'''
# os import to get cwd
import os
# pwinput to get password but hidden
from pwinput import pwinput
# datetime to get current date
import datetime


#====Login Section====


# Set login to true to later set to false when breaking out of loop when in another loop
login = True
while login:
    # Asks user for login details, password is case sensitive
    user_name = input("Please enter your user name: ").lower()
    
    password = pwinput("Enter password: ")
    # Gets all the user names and passwords and adding to login details
    with open(f"{os.getcwd()}\\Level_1\\Task_19\\user.txt", "r") as f:
        # Looping over lines in users.txt
        for line in f:
            # Getting username and passwords from each line
            user_name_line = line.split(", ")[0]
            password_line = line.split(", ")[-1].strip("\n")
            # Doing conditional checks 
            if user_name == user_name_line and password == password_line:
                print("Welcome!")
                # User name and password found so breaking out of while loop and for
                login = False
                break
            # If user name is found but not password
            elif user_name == user_name_line and password != password_line:
                print(f"{user_name} found but incorrect password") 
                break 
        # Both user name and password not found
        else:
            print("Invalid login: ")


while True:
    #presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    # Check if it is admin or not and displaying appropriate menu
    if user_name == "admin":
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
tn - view total number of tasks and users
e - Exit
: ''').lower()
    else:
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

    if menu == 'r': 
        if user_name == "admin":
            # All new users are saved in lower case
            new_user_name = input("Enter new user name: ").lower()
            # Doing check for user password and asking password again if not correct
            while True:
                new_user_password = pwinput("Please enter new password: ")
                password_check = pwinput("Please enter password again: ")
                if password_check == new_user_password:
                    break
                else:
                    print("Password doesn't match")
            # opening file in appending mode
            with open(f"{os.getcwd()}\\Level_1\\Task_19\\user.txt", "a") as f2:
                # Adding new user to end of list
                f2.write(f"\n{new_user_name}, {new_user_password}")
        
        else:
            print("You do not have permission to add users!")


    elif menu == 'a':
        # Asking user for all required information
        who_task = input("To whom is this task allocated to: ")
        task_title = input("Tile of the task: ")
        task_description = input("Enter a short description of the task\n: ")
        due_date = input("What is the due date of the task use dd mmm yyyy format: ")
        # Getting current date
        current_date = datetime.date.today().strftime("%d %b %y")
        # Opening file in append mode
        with open(f"{os.getcwd()}\\Level_1\\Task_19\\tasks.txt", "a") as f3:
            # Adding new task to end of list
            f3.write(f"\n{who_task}, {task_title}, {task_description}, {current_date}, {due_date}, No")

    elif menu == 'va':
        with open(f"{os.getcwd()}\\Level_1\\Task_19\\tasks.txt", "r") as f4:
            for line in f4:
                # This is done to remove \n
                task_com = line.split(', ')[-1].strip("\n")
                # Using print statements instead of \n to make code more readable
                print(f"\nTask:\t\t\t{line.split(', ')[1]}")
                print(f"Assigned to:\t\t{line.split(', ')[0]}")
                print(f"Date assigned:\t\t{line.split(', ')[3]}")
                print(f"Due date:\t\t{line.split(', ')[4]}")
                print(f"Task Complete?:\t\t{task_com}")
                print(f"Task description:\n{line.split(', ')[2]}\n\n")

    elif menu == 'vm':
        with open(f"{os.getcwd()}\\Level_1\\Task_19\\tasks.txt", "r") as f4:
            # Setting the amount of tasks users have to do
            user_tasks = 0
            for line in f4:
                # Checking if user is logged in is equal to the assigned name
                if user_name == line.split(', ')[0]:
                    #Adding to amount of tasks users have to do
                    user_tasks += 1
                    # This is done to remove \n
                    task_com = line.split(', ')[-1].strip("\n")
                    # Using print statements instead of \n to make code more readable
                    print(f"\nTask:\t\t\t{line.split(', ')[1]}")
                    print(f"Assigned to:\t\t{line.split(', ')[0]}")
                    print(f"Date assigned:\t\t{line.split(', ')[3]}")
                    print(f"Due date:\t\t{line.split(', ')[4]}")
                    print(f"Task Complete?:\t\t{task_com}")
                    print(f"Task description:\n{line.split(', ')[2]}\n\n")
            print(f"\nYou have {user_tasks} task/s to do.\n")
                
    # Check if user is admin so someone can't enter tn and still get access to this method
    elif menu == 'tn' and user_name == "admin":
        # Setting tasks and users to zero
        total_tasks = 0
        total_users = 0
        # Adding to their respected variable with each loop of line in file
        with open(f"{os.getcwd()}\\Level_1\\Task_19\\tasks.txt", "r") as f5:
            for line in f5:
                total_tasks += 1
        with open(f"{os.getcwd()}\\Level_1\\Task_19\\user.txt", "r") as f6:
            for line in f6:
                total_users += 1
        
        #Printing out in easy to read format
        print(f"\nThe total amount of users are: {total_users}")
        print(f"The total amount of tasks are: {total_tasks}\n")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")