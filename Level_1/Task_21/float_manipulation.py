# Importing math module 
import math
import re
from statistics import median

# Asking user for 10 numbers at once and making sure they are numbers
while True:
    user_input = input("Please enter 10 numbers separated by spaces. ")
    # Check that there is no alphabet characters
    if not re.findall("[A-Za-z]", user_input):
        # Check if ten numbers are entered
        if len(user_input.split()) == 10:
            break

# Creating list of floats
user_input_numbers = [float(i) for i in user_input.split()]

# Getting the total value off all items
print("Sum of all the numbers")
print(math.fsum(user_input_numbers))

# Getting the average of all values and rounding to two decimal place
print("Average")
print(f"{sum(user_input_numbers)/len(user_input_numbers):.2f}")

# Getting the median of all numbers
print("Median")
print(median(user_input_numbers))

# Getting the index of the max and min of the numbers
for i, num in enumerate(user_input_numbers):
    if num == max(user_input_numbers):
        print(f"The index of the max number is {i}")
    if num == min(user_input_numbers):
        print(f"The index of the min number is {i}")
