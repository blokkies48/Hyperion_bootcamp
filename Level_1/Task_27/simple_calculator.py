# Custom exception made from class inheritance from Exception https://www.programiz.com/python-programming/user-defined-exception
class OperationOutOfRange(Exception):
    pass

# Function made to do the operations
def operation_ans(number_1, number_2, operation_do):
    if operation_do == 1:
        return number_1 + number_2
    elif operation_do == 2:
        return number_1 - number_2
    elif operation_do == 3:
        try: # If user tries to divide by zero
            return number_1 / number_2
        except ZeroDivisionError:
            print("Unable to divide by zero") # None will be returned by function
    else:
        return number_1 * number_2

while True: # Making sure the user enters one of the options avoid logic errors
    user_input = input("1. Enter two numbers and a operation\n2. Open a file\nChoose 1 or 2: ")
    if "1" != user_input != "2":
        print("Please select one of the options given")
    else:
        break


if user_input == "1": # If user chose 1
    # Done to check that the user entered the correct values
    # Personal issue I have it that if a exception is raised at the end then the user will have to re-enter everything but I believe this approach is appropriate for the question
    while True:
        # Asking user for inputs and checking for errors
        try:
            number_1 = float(input("Enter first number: ")) # Float used so there can be decimal if user would like
            number_2 = float(input("Enter second number: "))
            operation_to_do = int(input('''Select a number 1,2,3,4
What operation would you like to be done to the 2 numbers entered
1. Plus
2. Subtract
3. Divide
4. Multiply
'''))
            # If user picks a number out of range then an exception is raised
            if 1 > operation_to_do or operation_to_do > 4:
                raise OperationOutOfRange
            break
        # Catching value errors due to inputs
        except ValueError:
            print("Please enter a number value")
        # Here if operation out of range is selected
        except OperationOutOfRange:
            print("Operation out of range")

    operation_dict = {1: "+", 2: "-", 3: "/", 4: "*"} # Dictionary used to get operator

    with open("output.txt", "a") as f: # No need to add exception handling because the with keyword is a resource manager that closes the file even if an exception is raised
        if operation_ans(number_1,number_2,operation_to_do) != None: # If none isn't returned by the operation function due to zero division then there won't be anything written to the file.
            f.write(f"\n{number_1} {operation_dict[operation_to_do]} {number_2} = {operation_ans(number_1,number_2,operation_to_do)}")
else: # If user chose 2
    while True: # Keeps asking user till file is found
        name_of_file = input("Enter the name of the file you want to open or q to quit: ")
        if name_of_file == "q": # This done incase there never is a file to end the program to avoid infinite loop
            quit()
        try:
            with open(f"{name_of_file}.txt", "r") as f: # Exception can be raised here
                for line in f: # Printing line for line
                    print(line)
                break
        except FileNotFoundError: # Catching the file not found error
            print("File does not exist! Try again")
        