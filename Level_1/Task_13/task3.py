#Setting count variable
count = 20
#While loop to count down to 0
while count >= 0:
    print(count)
    count -= 1

#Printing a new line of asterisks with one added
for i in range(1, 6):
    print("*" * i)

#Setting 2 number variables
num1 = 16
num2 = 12

#Checking for range in GCD in a range of one of the numbers provided
##Doesn't matter what num you use
for i in range(1,num1 + 1):
    #Checking if both mod the current number in range equals zero
    if num1 % i == 0 and num2 % i == 0:
        #Printing current number in range
        print(i) 
