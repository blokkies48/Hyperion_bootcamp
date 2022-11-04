# Base case if original string is empty


def search_replace(input_str, sub_str, replace_str,return_str = []): # Added another variable that is set to a empty list
    
    new_str = input_str.split(" ") # Sets input string to a list of the words
    word = new_str[0] # Getting the first word to compare


    if input_str == "": # If string is empty meaning we iterated over the whole string
        new_sen = " ".join(return_str) # Setting the return string to a new sentence
        return_str.clear() # Clearing the list so it doesn't get saved if you call the function again
        return new_sen # Returning created string

    # These two line ran after first if statement to avoid premature ending of function
    new_str.pop(0) 
    input_str = " ".join(new_str)

    # If the substring in the word then the replace function is ran on the word and the word is appended to the return string list and the function is returned
    if sub_str in word:
        return_str.append(word.replace(sub_str,replace_str))
        return search_replace(input_str, sub_str, replace_str,return_str)
    # Else just the word is just appended to the return string list
    else:
        return_str.append(word)
        return search_replace(input_str, sub_str, replace_str,return_str)
   
# Asking user inputs
input_string = input("Please enter a sentence\n:")
sub_string = input("Enter a sequence of characters you want to replace. Note no spaces allowed\n:")
replace_string = input("With what do you want to replace your sub-string with\n")


# Calling onto function and printing them
print(search_replace("Hello World how are you llo", "llo", "@@"))
print(search_replace(input_string,sub_string,replace_string))