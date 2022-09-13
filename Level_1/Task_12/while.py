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

# The reviewer said I didn't put in the logic for calculating the average.
# Maybe they missed it because I had a long comment underneath. Or am I missing something 
