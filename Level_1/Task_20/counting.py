# Counter used to count over string
from collections import Counter
# Regex used to only get alphabetic character
import re
# Setting original string
str1 = "google.com"

# Printing out counter class object
# Used regex to find all values in string
# Got this regex match from https://www.tutorialspoint.com/How-do-I-verify-that-a-string-only-contains-letters-numbers-underscores-and-dashes-in-Python#:~:text=Practical%20Data%20Science%20using%20Python&text=You%20can%20use%20regular%20expressions,9_%2D%5D*%24%22.
print(Counter(re.findall("[A-Za-z0-9_-]", str1)))


# Even the top result if perfectly usable this loop is used to give the result the question asked for.
# Setting original dict to empty
dict = {}
# Getting keys and values of each item in counter object
for key, value in Counter(re.findall("[A-Za-z0-9_-]", str1)).items():
    # Adding each key and value to new dict
    dict[key] = value

# Printing out new dict
print(dict)