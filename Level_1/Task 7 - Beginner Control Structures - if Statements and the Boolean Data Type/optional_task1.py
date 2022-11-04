#Asking user for a int number 
num1 = int(input("Please enter a whole number: "))

#Checking if number mod 2 is zero. Meaning it is a even number
if num1 % 2 == 0:
    print(f"{num1} is an even number ")
#Don't have to do a check again because all numbers that don't meet the above requirement is odd.
else:
    print(f"{num1} is an odd number ")