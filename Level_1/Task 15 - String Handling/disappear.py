# Asking user for a sentence input
sentence = input("Please input a sentence: ")
# Asking user for input letters to remove and removing spaces from input for later use
letters_to_strip = input("Enter letters you want to strip (seperate them with spaces)\nEnter Here: ").replace(" ","")

# Setting output string to empty 
sen2 = ""

# Looping over each letter in a sentence.
for letter in sentence:
    # Setting each letter to upper so input isn't case sensitive
    letter_up = letter.upper()
    # Checking if the letter upper is in the letters to strip upper this is done to remove case sensitivity
    if letter_up not in letters_to_strip.upper():
        # If the letter is not in the letters to strip it is added to the output string
        sen2 += letter

# Printing to output string
print(sen2)