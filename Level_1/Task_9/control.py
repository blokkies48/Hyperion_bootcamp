#Asking user for age input as an int
age = int(input("Please enter your age: "))

#Conditional statements to display using age variable
if age >= 18:
    print("You are old enough!")
elif 18 > age > 16:
    print("Almost there!")
else:
    print("You are too young!")