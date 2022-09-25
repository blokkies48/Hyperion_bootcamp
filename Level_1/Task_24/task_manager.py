#=====importing libraries===========
'''This is the section where you will import libraries'''
# os import to get cwd
import os
import time
# pwinput to get password but hidden
from pwinput import pwinput
# datetime to get current date
import datetime

#=====Function Section======
#Functions added with the code needed
def reg_user(user_name): # Passing in user name because it is needed for check
    if user_name == "admin":
        while True: # Two while loops used to not let the user re-enter everything if last condition isn't met
            # All new users are saved in lower case
            new_user_name = input("Enter new user name: ").lower()
            # Check done to see if user name already exists 
            with open("user.txt", "r") as f:
                    for line in f:
                        if new_user_name + "," in line: # comma added to not give an error when e.g john in johnny
                            print("Name in use")
                            break # breaks for loop
                    else:
                        break # Breaks while loop if for loop was never broken
        # Doing check for user password and asking password again if not correct
        while True:
            new_user_password = pwinput("Please enter new password: ")
            password_check = pwinput("Please enter password again: ")
            if password_check == new_user_password:
                break
            else:
                print("Password doesn't match")
            # opening file in appending mode
        with open("user.txt", "a") as f2:
            # Adding new user to end of list
            f2.write(f"\n{new_user_name}, {new_user_password}")
        
    else:
        print("You do not have permission to add users!")

def add_task(): # Function for adding task
    # Asking user for all required information
    # Keeping to lower to keep consistent with login and reg.
    who_task = input("To whom is this task allocated to: ").lower()
    task_title = input("Tile of the task: ")
    task_description = input("Enter a short description of the task\n: ")
    due_date = input("What is the due date of the task use dd mmm yyyy format: ")
    # Getting current date in required format
    current_date = datetime.date.today().strftime("%d %b %Y")
    # Opening file in append mode
    with open("tasks.txt", "a") as f3:
        # Adding new task to end of list
        f3.write(f"\n{who_task}, {task_title}, {task_description}, {current_date}, {due_date}, No")

def view_all(): # Function for viewing task
    with open("tasks.txt", "r") as f4:
        for line in f4:
            # This is done to remove \n
            task_com = line.split(', ')[-1].strip("\n")
            # Using print statements instead of \n to make code more readable
            print(f"\nTask:\t\t\t{line.split(', ')[1]}")
            print(f"Assigned to:\t\t{line.split(', ')[0].capitalize()}")
            print(f"Date assigned:\t\t{line.split(', ')[3]}")
            print(f"Due date:\t\t{line.split(', ')[4]}")
            print(f"Task Complete?:\t\t{task_com}")
            print(f"Task description:\n{line.split(', ')[2]}\n\n")

def view_mine(user_name): # Function viewing my tasks
    with open("tasks.txt", "r") as f4:
        #2d list used to store tasks and their data
        task_list = []
        user_task_list = []
        # Setting the amount of tasks users have to do
        user_tasks = 0
        for line in f4:
            # This is done to remove \n
            task_com = line.split(', ')[-1].strip("\n")
            # Creating the list of task data and storing the list in a list
            # index:data 0: task number
            task_list.append([line.split(', ')[0],line.split(', ')[1],line.split(', ')[2],line.split(', ')[3],line.split(', ')[4],task_com])
            # Checking if user is logged in is equal to the assigned name
            if user_name == line.split(', ')[0]:
                # Adding to user task list
                user_task_list.append([line.split(', ')[0],line.split(', ')[1],line.split(', ')[2],line.split(', ')[3],line.split(', ')[4],task_com])
                #Adding to amount of tasks users have to do
                user_tasks += 1
                # Using print statements instead of \n to make code more readable
                print(f"\nTask number:\t\t\t{user_tasks}")
                print(f"Task:\t\t\t{line.split(', ')[1]}")
                print(f"Assigned to:\t\t{line.split(', ')[0].capitalize()}")
                print(f"Date assigned:\t\t{line.split(', ')[3]}")
                print(f"Due date:\t\t{line.split(', ')[4]}")
                print(f"Task Complete?:\t\t{task_com}")
                print(f"Task description:\n{line.split(', ')[2]}\n\n")
        print(f"\nYou have {user_tasks} task/s to do.\n")

        # This removes the items that are to be changed from the task list 
        # list com form https://stackoverflow.com/questions/36268749/how-to-remove-multiple-items-from-a-list-in-just-one-statement
        task_list = [item for item in task_list if item not in user_task_list]
        # This only happens if the user has tasks to do
        if user_tasks > 0:
            # Getting the task from the list for the user.
            user_task_select = int(input("Choose the number of the task you want or -1 to skip\n: "))
            # Check done to to make user user selects a number in the range of tasks they have
            if user_task_select != -1 and user_task_select <= user_tasks:
                is_complete = input("Want to edit (e) or Is this task done? (y/n)? ").lower()       
                if is_complete == "y": # If y is chosen
                    user_task_list[user_task_select -1][5] = "Yes" # Returning the list at the index the user choose.
                elif is_complete == "e" and user_task_list[user_task_select -1][5] == "No":  # Ran if user choses edit and task has not been completed yet
                    # Letting user choose what they want to change
                    what_to_change = input("What do you want to change?\nPerson assigned to task (a)\nDue date (d)\nBoth (b)\n").lower()
                    if what_to_change == "a":
                        user_task_list[user_task_select -1][0] = input("To whom would you like to assign this task to: ").lower() # Changing to who the task is assigned to
                    elif what_to_change == "d":
                        user_task_list[user_task_select -1][4] = input("To whom would you like to assign this task to: ").lower() # Changing the due date
                    else:
                        # Changing both
                        user_task_list[user_task_select -1][0] = input("To whom would you like to assign this task to: ").lower() # Changing to who the task is assigned to
                        user_task_list[user_task_select -1][4] = input("What is the due date of the task use dd mmm yyyy format: ").lower() # Changing the due date
            task_list.extend(user_task_list)  
            # Rewrites changes to the file 
            with open("tasks.txt", "w+") as f4:
                for index in range(0, len(task_list)):
                    f4.write(", ".join(task_list[index]))
                    # This done to avoid adding line at the end
                    if index < len(task_list) -1:
                        f4.write("\n")
                
def total_func(): # func for getting totals this was done in previous task just added it into it's own function
    # Setting tasks and users to zero
    total_tasks = 0
    total_users = 0
    # Adding to their respected variable with each loop of line in file
    with open("tasks.txt", "r") as f5:
        for _ in f5:
            total_tasks += 1
    with open("user.txt", "r") as f6:
        for _ in f6:
            total_users += 1
            # Printing out in easy to read format
    print(f"\nThe total amount of users are: {total_users}")
    print(f"The total amount of tasks are: {total_tasks}\n")

def generate_reports():
    # Setting all the totals to 0
    total_tasks_r = 0
    total_complete = 0
    total_uncompleted = 0
    total_overdue = 0
    with open("tasks.txt", "r") as f5:
        for line in f5: # looping over lines
            total_tasks_r += 1 # Adding to total tasks
            if "Yes" in line: # adding if task is completed
                total_complete += 1
            if "No" in line: # adding if tasks isn't completed
                total_uncompleted += 1
            # Comparing the two dates with formatting dates to datetime objects and comparing objects 
            if datetime.datetime.strptime(datetime.date.today().strftime("%d %b %Y"), "%d %b %Y") > datetime.datetime.strptime(line.split(', ')[4], "%d %b %Y") and "No" in line:
                total_overdue += 1
    # Generating task_overview file
    with open("task_overview.txt", "w") as r:
        # Printing out as the question asks
        r.write(f"The total amount of tasks are: {total_tasks_r}\n")
        r.write(f"The total amount of completed tasks are: {total_complete}\n")
        r.write(f"The total amount of uncompleted tasks are: {total_uncompleted}\n")
        r.write(f"The total amount of overdue are: {total_overdue}\n")
        r.write(f"The total percentage of tacks completed: {(total_complete/total_tasks_r)*100:.2f}%\n")
        r.write(f"The total percentage of tacks overdue: {(total_overdue/total_tasks_r)* 100:.2f}%\n")

    # Opening user file to get user name and amount of users
    with open("user.txt", "r") as f:
        total_users_r = 0
        user_names = []
        for line in f:
            total_users_r += 1   
            user_names.append(line.split(", ")[0])

    # Generating user_overview
    with open("user_overview.txt", "w") as r:
        r.write(f"The total amount of users are: {total_users_r}\n")
        r.write(f"The total amount of tasks are: {total_tasks_r}\n")
        r.write("Users are: \n")
        # Looping over list of names
        for name in user_names:
            # Setting variables to 0
            users_task = 0
            users_task_completed = 0
            users_task_uncompleted = 0
            overdue_task = 0
            # Opening task for info to do comparisons with
            with open("tasks.txt", "r") as f:
                # Looping over each line
                for line in f:
                    # Doing comparisons and adding where needed for each name
                    if name + "," in line:
                        users_task += 1
                    if name + "," in line and "Yes" in line:
                        users_task_completed += 1
                    if name + "," in line and "No" in line:
                        users_task_uncompleted += 1
                    # Same logic as above
                    if datetime.datetime.strptime(datetime.date.today().strftime("%d %b %Y"), "%d %b %Y") > datetime.datetime.strptime(line.split(', ')[4], "%d %b %Y") and "No" in line and name + "," in line:
                        overdue_task += 1
            # Writing to user_overview
            try: # Try this because of zero division
                r.write(f"\tUser: {name.capitalize()}\n")
                if users_task == 0: # Used to throw exception to not have to print unnecessary info
                    raise ZeroDivisionError
                r.write(f"\t\tUser's tasks: {users_task}\n")
                r.write(f"\t\tCompleted tasks: {users_task_completed}\n")
                r.write(f"\t\tUncompleted tasks: {users_task_uncompleted}\n")
                r.write(f"\t\tUser has {(users_task/total_tasks_r)*100:.2f}% of all tasks\n")
                r.write(f"\t\tUser has completed {(users_task_completed/users_task)*100:.2f}% of their tasks\n")
                r.write(f"\t\tUser has to complete {(users_task_uncompleted/users_task)*100:.2f}% of all tasks\n")
                r.write(f"\t\tUser has {(overdue_task/users_task)*100:.2f}% overdue of all tasks\n")
            except ZeroDivisionError: # If no tasks are available for user then a exception is raised
                r.write("\t\tThis user has no tasks\n")
# Displaying stats
def display_stats():
    # Just opening the files and writing to console because I already made the text files user friendly
    print("\nDetailed info on users\n------")
    with open("user_overview.txt", "r") as r: # Getting detailed info first
        for line in r:
            print(line)
    print("\nOverall general info\n------")
    with open("task_overview.txt", "r") as r: # Displaying general info after
        for line in r:
            print(line)


#====Login Section====

# Set login to true to later set to false when breaking out of loop when in another loop
login = True
while login:
    # Asks user for login details, password is case sensitive
    user_name = input("Please enter your user name: ").lower()
    
    password = pwinput("Enter password: ")
    # Gets all the user names and passwords and adding to login details
    with open("user.txt", "r") as f:
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
gr - generate reports
ds - display statistics
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
        reg_user(user_name) # Passing user name to function

    elif menu == 'a':
        add_task() # Calling on add task function

    elif menu == 'va':
        view_all() # Calling view all function
    

    elif menu == 'vm':
        view_mine(user_name) # Calling view mine function/ Passing user name to find the user
                
    # Check if user is admin so someone can't enter tn and still get access to this method
    elif menu == 'tn' and user_name == "admin":
        total_func()
    
    elif menu == 'gr' and user_name == "admin": # Generate report for admin only
        generate_reports()

    # Displaying stats to console but first generating the reports 
    elif menu == 'ds' and user_name == "admin":
        generate_reports()
        display_stats()



    # Code from template
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")