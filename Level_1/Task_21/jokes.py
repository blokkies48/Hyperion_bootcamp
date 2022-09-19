from random import randint # Using randint to get back the index of a joke
import os # os used to get cd because jokes stored in a text file


# Opening file with jokes. Jokes from https://parade.com/1040121/marynliles/one-liners/
with open(f"{os.getcwd()}\\Level_1\\Task_21\\jokes.txt","r") as f:
    # jokes = [] # List of jokes created because questions asks for it. but not needed 
    random_joke = randint(0,19)  # Getting index of the joke 
    for i, line in enumerate(f): # Iterating over the jokes and indexes
        # jokes.append(line) # Adding to joke list
        if i == random_joke:  # Checking for a joke index that matches the random int
            print(line.strip("\n")) # Printing joke
    # print(jokes[random_joke].strip("\n")) # Printing joke with random index

# List not used because not need to take up unnecessary memory, but did include how you would go about using it. For the question