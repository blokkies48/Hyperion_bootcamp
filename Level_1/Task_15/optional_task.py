# Asking user to enter a word or phrase to compare
# Removing spaces to check phrases and setting to lower so it isn't case sensitive.
word_or_phrase = input("Enter a word or phrase to check if it is a palindrome.\n:").replace(" ", "").lower()

# Whecking if input is the same forwards and backwards and printing appropriate statements
if word_or_phrase == word_or_phrase[::-1]:
    print("Your word/phrase is a palindrome.")
else:
    print("Youe word/phrase is not a palindrome.")