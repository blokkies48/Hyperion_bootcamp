
#Asking user for data to calculate the total price
price_of_package = float(input("Please enter the price of a package you would like to purchase: "))
distance_kms = float(input("Please enter the distance the package has to travel: "))

#Making sure user understands instrutions
print("Please enter 1 or 2 only!")

#Asking for inputs to use in conditional statements
by_air_or_not = input("Travel by air? enter 1, travel by freight? enter 2: \n")
insurance_get = input("Do you want full insurance? R50.00 enter 1. or for limited? R25.00 enter 2: \n")
gift = input("Add a gift of R15.00 press 1:\n")
priority = input("For priority enter 1 (R100) or for standard enter 2 (R20)")

#Setting total price to equal price of package initially
total_price = price_of_package

#Calculating the price with conditional statements.
if by_air_or_not == "1":
    total_price += (distance_kms * 0.36)
else:
    total_price += (distance_kms * 0.25)

if by_air_or_not == "1":
    total_price += 50.00
else:
    total_price += 25.00

#Note no need for else statement because there is no modifications to the total price
if gift == "1":
    total_price += 15.00

if priority == "1":
    total_price += 100.00
else:
    total_price += 20

#Printing total and rounding it to 2 decimal space
print(f"The total price will cost R{round(total_price,2)}")




