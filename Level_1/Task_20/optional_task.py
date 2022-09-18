# Setting original dictionary
abbs = {"lol": "Lots of love", "mfw": "My face when", "jk": "Just kidding", "ily": "I loathe you" }

# Adding another 2 items to the dictionary
abbs["ifyp"] = "I feel your pain"
abbs["idc"] = "I don't care"

# Asking user for abbreviation and setting it to lower to match dictionary keys
user_input = input("Please enter a abbreviation you want to know: ").lower()

# Iterating over the items in the dictionary
for key, value in abbs.items():
    # If the key is equal to the user input then value is printed
    if key == user_input:
        print(value.title())
        # Breaks out of loop because it is no longer needed to check for another abb
        break
else:
    # Printing out if loop is never broken
    print("Abbreviation not found")