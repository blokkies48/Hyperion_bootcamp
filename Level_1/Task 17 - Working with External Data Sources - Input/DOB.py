# Importing os to get current working directory
import os
# Importing re to find in a string
import re

# Made two methods to get the names and DOB to reduce code in main method
# Takes in the line and uses regular expressions to remove digits from string and turning it into a list then getting the first item in list. 
# This will work even if the person has more than two names
def get_name(line):
    return re.findall(r'\D+', line)[0]

# Getting DOB with regex returning it as a string.
# Scalable but won't work if formatting changes
def regex_DOB(line):
    return re.findall(r'(\d+.\w+.\d+)', line)[0]
    

# Saved file on my own machine in the folder where I am doing the bootcamp in 
with open(f"{os.getcwd()}\\Level_1\\Task_17\\DOB.txt", "r") as f:
    # Setting name and dates variable to empty
    name = ""
    dates = ""
    # Looping over every item in a list
    for line in f:
        # Setting name and dates to equal the name plus new line and the name or date gotten from each line
        name = name + "\n" + get_name(line)
        dates = dates + "\n" + regex_DOB(line)


# Printing names and dates with the appropriate format.
print(f"\nName:{name}\n")
print(f"\nBirthdate:{dates}\n")

# Adding a new text file with content on.
with open(f"{os.getcwd()}\\Level_1\\Task_17\\Names_DOB.txt", "w+") as f2:
    f2.write("This file contains names and DOB separated\n")
    f2.write(f"\nName:{name}\n")
    f2.write(f"\nBirthdate:{dates}\n")


