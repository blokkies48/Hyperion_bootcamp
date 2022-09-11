#Different approach to having a if statement to break the loop
#I personally prefer the if statement but this is just to display another way
#Setting a initial variable to use for while loop
num_input = 0

#List for numbers entered
enter_numbers = []
while num_input != -1:
    num_input = int(input("Please input a whole number or -1 to stop "))

    #Appending input to list
    enter_numbers.append(num_input)

#Because we are not using if statement we will have to pop off the last number in the list that will always be -1
enter_numbers.pop()

#Calculating the average and printing it 
average = sum(enter_numbers)/len(enter_numbers)
print(average)

'''
I believe for this instance not using a check for -1 inside of the loop is better because if you have a million numbers your programme won't have to check each number again.

Same can be said for names.py but personally I feel having that if statement makes the code more readable and looks neater.

Where while true will be better is for a programme that has to do something and just check if input condition has been met or is correct and not adding or iterating over lists because it won't scale well.

Please can you state if my assesment is correct or not sorry for diverting so far from the question. I will appriciate it a lot. Thank you!
'''
