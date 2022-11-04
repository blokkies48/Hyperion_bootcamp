#Initiating while loop to true
while True:
    #Asking user to input a number
    number_entered = int(input("Please enter a whole number equal to or less than 100\n:")) 
    #Checking that the number is less than or equal to 100
    if number_entered <= 100:
        #Checking if even or not and printing appropriate arithmatic.
        #Then breaking out of loop
        if number_entered % 2 == 0:
            print(number_entered * 2)
            break
        else:
            print(number_entered * 3)
            break

'''As mentioned in the while.py. This optional task is the perfect use of a while true loop'''