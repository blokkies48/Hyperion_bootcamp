num1 = 100
num2 = 200
num3 = 300

#Checking for largest between 2 numbers
if num1 > num2:
    print(num1)
else:
    print(num2)

#Checking if num num1 is even or odd
if num1 % 2 == 0:
    print("Even")
else:
    print("Odd")

#Comparing numbers and printing out from largest to smallest
if num2 < num1 > num3:
    print(num1)
    if num2 > num3:
        print(num2)
        print(num3)
    else:
        print(num3)
        print(num2)
elif num1 < num2 > num3:
    print(num2)
    if num1 > num3:
        print(num1)
        print(num3)
    else:
        print(num3)
        print(num1)
elif num2 < num3 > num1:
    print(num3)
    if num1 > num2:
        print(num1)
        print(num2)
    else:
        print(num2)
        print(num1)

