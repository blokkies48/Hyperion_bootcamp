# Setting list of names to empty
names = []

while True:
    # Asking user for name input
    name = input("Enter a name and enter John to stop\n: ")
    # Breaking out of loop if name is John. Code will stop running if condition is met that why there is no else statement
    if name.upper() == "JOHN": break
    # If isn't John then it is added to the end of the list
    names.append(name.capitalize()) # Just incase user didn't cap each name

# Printing list with names
print(names)



