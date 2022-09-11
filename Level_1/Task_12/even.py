#Asking user for initial number 
number = int(input("Please enter a whole number: "))
#Setting count to one so and not 0 so 0 isn't printed
count = 1

#Checking while count not equal to number plus one do
#Number plus one is to print the last number if it is even
while count != number + 1:
    #Checking if number is even
    if count % 2 == 0:
        print(count)
    #Increasing count by 1 with every loop
    count += 1

