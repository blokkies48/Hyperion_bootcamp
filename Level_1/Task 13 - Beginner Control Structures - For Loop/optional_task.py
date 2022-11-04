#Ask user for input
num = int(input("Please enter a whole number: "))

#Checking the size of the number
#If it smaller or equal to ten
if num <= 10:
    print("Sorry too small")
#Else print num in range of num
else:
    for i in range(num):
        print(num)