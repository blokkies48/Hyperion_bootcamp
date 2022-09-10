#Importing math libary for later use
import math

#Printing menu with one print command
print("\nChoose either 'investment' or 'bond' from the menu below to proceed:\n\ninvestment\t-\tto calculate the amount of interest you'll earn on your investment\nbond\t\t-\tto calculate the ammount you'tt have to pay on a home loan")

#Making sure user understands what to do
#Looping till correct input is given
while True:
    print("\nPlease enter the full name (investment/bond) and spelled correctly.")
    menu_item_selected = input("Enter choice here: ")

    #If user selected investment
    if menu_item_selected.upper() == "INVESTMENT":
        #Bunch of while loops with try and except to make sure user inputs are correct
        #Try used because an exception is raised if you try input something that's not a digit
        while True:
            try:
                #Using float throughout the code because there can be decimal value for each input
                amt_depositing = float(input("Money you want to deposit: "))
                break
            except ValueError:
                print("Invalid value")
        while True:
            try:
                interest_rate = float(input("Please enter the interest rate don't use %: "))/100
                break
            except ValueError:
                print("Invalid value")
        while True:
            try:
                years = float(input("How many years do you want to invest: "))
                break
            except ValueError:
                print("Invalid value")

        #To check if user enters correct input when asking for interest type
        while True:
            print("\nDo you want simple or compound interest?\n\nEnter simple or compound only. ")
            interest_type = input("Enter here: ")
            if interest_type.upper() == "SIMPLE":
                total_returns = amt_depositing*(1 + interest_rate * years) 
                break
            elif interest_type.upper() == "COMPOUND":
                total_returns = amt_depositing * math.pow((1+interest_rate),years)
                break

        #Printing your total return in two decimal place
        print(f"Your total return are R{round(total_returns,2)}")
        #Breaking main loop
        break

    #If user entered bond
    elif menu_item_selected.upper() == "BOND":

        #Make sure user enters correct values with while loops and try except values
        while True:
            try:
                value_of_bond = float(input("Enter value of bond: "))
                break
            except ValueError:
                print("Invalid value")

        while True:
            try:
                interest_rate = float(input("Enter the annual interest rate ignore '%' symbol: "))/100
                monthly_interest = interest_rate/12
                break
            except ValueError:
                print("Invalid value")

        while True:
            try:
                months = float(input("How many months do you want to repay: "))
                break
            except ValueError:
                print("Invalid value")

        repayment = (monthly_interest * value_of_bond)/(1 - (1 + monthly_interest)**(-months))
        #Printing repayment amount and total to be paid
        print(f"The amount to be paid per month is R{round(repayment,2)}")
        print(f"Total amount to be paid is R{round((repayment * months),2)}")
        #Breaking main loop
        break
    

