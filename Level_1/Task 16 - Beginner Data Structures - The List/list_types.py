# List of friend names. Hard coded
friends_names = ["Tim Walker", "Tom Daniels", "Terry Cruise"]

# Index used to compare indexes rather than strings. This is done incase there are 2 people with the same names
# Looping over list of full names
for index_count, name in enumerate(friends_names):
    # Always getting the first and last name in list 
    if index_count == 0 or index_count == len(friends_names) - 1:
        print(name)
    # Increasing index by 1
    index_count += 1

# Printing original string's length as asked in question
print(len(friends_names))

# Storing ages of friends. Question doesn't state what should be done just asks for the list
friends_ages = [22, 23, 24]


