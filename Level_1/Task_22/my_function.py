# Func that just prints out days of the week
def print_day_week():
    print("Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday")

# Func that takes a sentence and replaces every second word with hello
def hello(sen):
    # Splitting sentence passed to a list
    sen_list = sen.split()
    # Setting return list to false
    return_list = []
    # Enumerating over list with words in the sentence
    for i, word in enumerate(sen_list):
        # Using index to find every second word
        if (i + 1) % 2 == 0:
            # If it is a even num appends hello to list
            return_list.append("Hello")
        else:
            # Else it appends the word
            return_list.append(word)
    # Returning string of the list
    return " ".join(return_list)

# Printing week days using function
print_day_week()

# Printing the hello function with sentence passed
print(hello(input("Please enter a sentence\n")))
