#Setting initial variables
temp_g_20 = True
is_weekend = True
is_sunny = True

print("Please enter yes or no only.")

#Asking user for inputs of the 3 conditions required
##Setting to true or false depending on inputs
###(Extra) You can wrap each condition in a while True loop and break if a condition is met to make sure the user enters correctly.
temp_input = input("Is the temperature greater than 20 degrees?\n")
if temp_input.upper() == "YES":
    temp_g_20 = True
if temp_input.upper() == "NO":
    temp_g_20 = False

is_weekend_input = input("Is it weekend?\n")
if is_weekend_input.upper() == "YES":
    is_weekend = True
if is_weekend_input.upper() == "NO":
    is_weekend = False

is_sunny_input = input("Is it sunny?\n")
if is_sunny_input.upper() == "YES":
    is_sunny = True
if is_sunny_input.upper() == "NO":
    is_sunny = False

#Setting outfit to empty to initially
outfit = ""

#Using set variables to create outfit by adding to the end of the string
if temp_g_20:
    outfit = outfit + "A short-sleeved shirt, "
if not temp_g_20:
    outfit = outfit + "A long-sleeved shirt, "

if is_weekend:
    outfit = outfit + "with shorts "
if not is_weekend:
    outfit = outfit + "with jeans "

if is_sunny:
    outfit = outfit + "and a cap. "
else:
    outfit = outfit + "and a raincoat "

print(outfit)