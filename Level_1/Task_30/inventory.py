
#========The beginning of the class==========
class Shoe:
    # Constructing all the values
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return float(self.cost) # Return float value
    

    def get_quantity(self):
        return int(self.quantity) # Return int value

    
    def get_code(self): # Added function to make it easier for myself in search func
        return self.code

    # Neatly formatted string returned
    def __str__(self):
        return f"Country: {self.country}\nCode: {self.code}\nProduct: {self.product}\nCost: R{float(self.cost):.2f}\nQuantity: {self.quantity}"

     


#=============Shoe list===========


shoe_list = [] # Came with temp



#==========Functions outside the class==============
# Getting all the shoes function and store each shoe object into a list

def read_shoes_data():
    # No need to use try and except with the "with" keyword
    # Because it still closes the file if an error occurred
    with open("inventory.txt", "r") as shoes: # Opening inventory
        next(shoes) # Skip the first line
        for  line in shoes: # enumerate to get the first index
            line_list = line.replace("\n","").split(",") # Splitting the line to a list
            # Creating shoe object from getting list indexes
            shoe = Shoe(
                country = line_list[0],
                code = line_list[1],
                product = line_list[2], 
                cost = line_list[3],
                quantity = line_list[4]) 
            shoe_list.append(shoe) # Adding shoe object to the list

def capture_shoes():
    # To keep consistent and append to file easier
    country = input("Country: ")
    code = input("Code: ").upper()
    product = input("Product: ") 
    # Making user user enters a valid number
    while True:
        try:
            cost = float(input("Cost: "))
            quantity = int(input("Quantity: "))
            break
        # If user entered an incorrect value they will be asked to try again
        except ValueError: 
            print("Enter valid number value")
    # Creating shoe object to add to the list
    shoe = Shoe(
            country=country,
            code=code,
            product=product,
            cost=cost,
            quantity=quantity
            )
    # Appending shoe to list
    shoe_list.append(shoe)
    # Appending shoe to file
    with open("inventory.txt", "a") as shoes:
        shoes.write(f"\n{country},{code},{product},{cost},{quantity}")
    


def view_all():
    for shoe in shoe_list:
        print() # have spaces between shoes so make it easier to read
        print(shoe) # Printing shoe object according to __str__ func


def re_stock():
    # Algorithm to find the lowest quantity
    lowest_num = shoe_list[0].get_quantity()  # Setting the lowest value to the first item on the list
    for index, shoe in enumerate(shoe_list): # Looping over all the shoes
        if (shoe.get_quantity()) < lowest_num: # If the current shoe's quantity is lower than the current lowest quantity
            lowest_num = (shoe.get_quantity()) # Setting the new lowest number
            lowest_shoe = shoe # Setting the new lowest 
            i = index # used to mod item in list later
    # Displaying lowest quantity to the user
    print("Shoe with lowest quantity:")
    print(lowest_shoe)
    # If user doesn't enter a valid option they will be given an error message and asked to enter again
    while True: 
        # Asking if they want to update lowest quantity
        user_input = input("Do you want to update the stock (y/n): ").lower()
        if user_input == "y": # If yes
            # Setting new quantity where index is used form above
            shoe_list[i].quantity = input("New Quantity: ") # Do not cast to int to makesmod to file easier.
            with open("inventory.txt", "w") as shoes: # Opening file
                shoes.write("Country,Code,Product,Cost,Quantity") # Have to rewrite everything
                # Writing each line to file again
                for shoe in shoe_list:
                    shoes.write(f"\n{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}")
            break # Breaks loop
        elif user_input == "n":
            break # Breaks loop
        else:
            print("Invalid input please try again") # Error message given to user

# This function works with the letter prefix to the id
# This is due to the fact later on the prefix might change
# And not all will be the same
def search_shoe():
    search_input = input("Code to search: ").upper()
    for shoe in shoe_list:
        if shoe.get_code() == search_input:
            return shoe
    else:
        return "Shoe not found"


def value_per_item():
    # looping over shoe list
    for shoe in shoe_list:
        # Multiple print statements to make code more readable
        print()
        print(shoe)
        print("--Total value of this item--")
        print("R{:.2f}".format(shoe.get_cost() * shoe.get_quantity()))

def highest_qty():
    # Same logic as lowest_qty func just where lowest is used highest will be used
    highest_num = shoe_list[0].get_quantity()  # Setting the highest value to the first item on the list
    for shoe in shoe_list: # Looping over all the shoes
        if (shoe.get_quantity()) > highest_num: 
            highest_num = (shoe.get_quantity()) 
            new_shoe = shoe 
            
    print("Shoe is on sale!!")
    print(new_shoe)
    # Added new price just for fun
    # Because it is out of the scope of the task
    while True:
        try:
            sale_percentage = int(input("Enter discount percentage: "))
            percentage_amount = 1 - (sale_percentage/100) 
            print("The sale price is") 
            print("{:.2f}".format(new_shoe.get_cost() * percentage_amount))
            break
        except:
            print("Enter valid number.")




#==========Main Menu=============

def main(): # Main func will have all the code that needs to be ran
    read_shoes_data() # This function needs to be ran when starting the programme
    while True:
        # Asking user for inputs
        print("\nPlease select an option")
        print("Enter a number 1 through 5")
        user_choice = input("1. Log shoe\n2. View current stock\n3. Re-stock a shoe\n4. Search for an item\n5. Value of each item\n6. Highest value item\n7. quit\nEnter a number 1 through 7\n:")

        # Comparing user input 
        # Standard checks then related function is ran
        if user_choice == "1":
            capture_shoes()
        elif user_choice == "2":
            view_all()
        elif user_choice == "3":
            re_stock()
        elif user_choice == "4":
            print(search_shoe())
        elif user_choice == "5":
            value_per_item()
        elif user_choice == "6":
            highest_qty()
        elif user_choice == "7":
            print("Goodbye")
            break # When quitting 
        else:
            print("Please enter a valid value") # If no values entered match

if __name__ == "__main__":
    main() # Calling main function to be ran


