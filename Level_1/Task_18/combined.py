# randint imported to generate random lists
from random import randint
# regex used to find digits
import re
#Asking user how many files they want to generate. 
# While loop to make sure user doesn't break their machine
while True:
    print("Please don't enter a large number! Keep between 2 and 5")
    range_num = int(input("How many files do you want to generate\n: "))
    if 1 < range_num < 6: break

# Setting empty file variable 
files = []
# creating files depending on a range.
# You can generate more files if you want to
for i in range(1,range_num+1):
    with open(f"numbers{i}.txt", "w+") as f_num_1:
        # Generating the random list
        numbers = [randint(1,99) for _ in range(randint(1,99))]
        # Sorting the list in ascending order or descending depending on if statement
        # Positive num is descending and odd in ascending
        if i % 2 != 0:
            numbers.sort()
        else:
            numbers.sort(reverse=True)
        # Writing numbers to file
        f_num_1.write(" ".join(str(num) for num in numbers))
    # Appending the current file name to variable list
    files.append(f"numbers{i}.txt")

# Creating a all numbers file and getting all numbers from all files.
# Adding them in ascending order
with open("all_numbers.txt", "w+") as f_num_3:
    # Setting unsorted nums to empty list for later use
    unsorted_nums = []
    # Opening all files in above list
    for file in files:
        with open(file, "r") as f:
            # Getting the numbers out of file
            unsorted_nums += re.findall(r"\d+", f.read())
    # This is done to get int otherwise a single digit is read as a double digit. e.g 5 is seen as 50
    # I am not sure why and can't find an answer
    sorted_nums = [int(i) for i in unsorted_nums]
    # Writing sorted numbers in all num file
    for num in sorted(sorted_nums):
        f_num_3.write(str(num) + " ")
