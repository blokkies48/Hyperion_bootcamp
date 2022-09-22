# The modules that I like to use in these tasks
import os
import re
from random import randint

# Getting the min of an argument
def min_func(args):
    return min(args)

# Getting the max of an argument
def max_func(args):
    return max(args)

# Getting the average of an argument
def average_func(args):
    return sum(args)/len(args)

# Bonus task - 
# Getting the percentile
def percentile(p,list1):
    list1.sort()
    index_po = round((p/100) * len(list1)) - 1 # Getting the position of the percentile
    return list1[index_po] # Returning the number at that position


# Asking user if they want to generate random numbers or use the file included in the question.
user_input = input("Do you want to use random generated numbers or not (y/n): ").lower()

if user_input == "y": # File only generated if user asks for random
    # Used to generate random numbers to add to the challenge
    with open(f"{os.getcwd()}\\input_random.txt", "w+") as f:
        dict = {0: "Min", 1: "Max", 2: "Average", 3: "Percentile"} # Dictionary with key as int and value as the name
        i = 0 # i used to get key from dictionary
        while i <= len(dict) - 1: # Loops while i is smaller or equal to len of dict - 1
            if i != len(dict) - 1:
                f.write(f"{dict[i]}: {[randint(1,99) for x in range(10)]}\n") # Writing to each line with dict key's value and a list of random ints
            else:
                f.write(f"{dict[i]} {(randint(1,10)) * 10}: {[randint(1,99) for x in range(10)]}\n") # Used to write Percentile need another value % that why it is separated
            i += 1 # Incrementing i by 1

# Checks done to see what user choose and setting file names accordingly
if user_input == "y":
    file_name = "input_random"
else:
    file_name = "input"

with open(f"{os.getcwd()}\\{file_name}.txt", "r") as f: # opening input depending on choice with read mode
    values_list = [] # Empty list to store tuples of values to use later
    for line in f: # Looping over each line
        # If statements  used to check the values from the dictionary
        if "Min" in line: # If min is in the line
            list_min_nums = [int(i) for i in re.findall(r"\d+", line)] # Getting all the numbers in min line and turing them into ints
            values_list.append(("Min", list_min_nums)) # Tuple added to list
        if "Max" in line: # If max is in the line
            list_max_nums = [int(i) for i in re.findall(r"\d+", line)] # Getting all the numbers in max line and turing them into ints
            values_list.append(("Max", list_max_nums)) # Tuple added to list
        if "Average" in line: # If average is in the line
            list_average_nums = [int(i) for i in re.findall(r"\d+", line)] # Getting all the numbers in average and turing them into ints
            values_list.append(("Average", list_average_nums)) # Tuple added to list
        if "Percentile" in line or "p" in line: # If percentile is in the line
            list_percentile_nums = [int(i) for i in re.findall(r"\d+", line)] # Getting all the numbers in average and turing them into ints
            percentile_value = list_percentile_nums.pop(0)
            list_percentile_nums.sort()
            values_list.append(("Percentile",percentile_value, list_percentile_nums)) # Tuple added to list
        if "Sum" in line: # Added sum for optional question
            list_sum_nums = [int(i) for i in re.findall(r"\d+", line)]
            values_list.append(("Sum", list_sum_nums))


with open(f"{os.getcwd()}\\output.txt", "w") as f2: # Opening and writing to output.txt
    # Using f strings with self made functions in them
    for tuple_v in values_list: 
        if tuple_v[0] == "Min": # Comparing index 0 of tuples to strings
            # Unpacking tuples to get the needed info and writing it to file for each
            f2.write(f"The {tuple_v[0]} of {tuple_v[1]} is {min_func(tuple_v[1])}\n")
        if tuple_v[0] == "Min":
            f2.write(f"The {tuple_v[0]} of {tuple_v[1]} is {max_func(tuple_v[1])}\n")
        if tuple_v[0] == "Average":
            f2.write(f"The {tuple_v[0]} of {tuple_v[1]} is {average_func(tuple_v[1])}\n")
        if tuple_v[0] == "Percentile":
            f2.write(f"The {tuple_v[0]} {tuple_v[1]} of {tuple_v[2]} is {percentile(tuple_v[1],tuple_v[2])}\n") # Adding percentile
        if tuple_v[0] == "Sum":
            f2.write(f"The {tuple_v[0]} of {tuple_v[1]} is {sum(tuple_v[1])}\n")