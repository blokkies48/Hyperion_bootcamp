#Declaring variables
num1 = 99.23
num2 = 23
num3 = 150
string1 = "100"

#Converting variables
num1 = int(num1)
num2 = float(num2)
num3 = str(num3)
string1 = int(string1)

#Printing out variables to console
print(f"{num1}\n{num2}\n{num3}\n{string1}")

#Check that conversion happened
print(f"{type(num1)}\n{type(num2)}\n{type(num3)}\n{type(string1)}")