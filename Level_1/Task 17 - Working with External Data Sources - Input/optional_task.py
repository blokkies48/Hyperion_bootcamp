# Importing os to get cwd
import os
from tkinter import W
from turtle import title
import lxml

# getting text from website just generate random text for task making it more challenging
import requests
from bs4 import BeautifulSoup
URL = "https://www.lipsum.com/feed/html"
file = requests.get(URL)
soup = BeautifulSoup(file.content, "lxml")


# Creating a new file in this directory
with open(f"{os.getcwd()}\\Level_1\\Task_17\\input.txt", "w") as f:
    # Lorem ipsum used from https://www.lipsum.com/ and grabbing 5 paragraphs
    for i in range(5):
        f.write(soup.select("p")[i].getText())
    

# Decided to do 2 different methods because it is a bonus task

# Opening same file again to read
with open(f"{os.getcwd()}\\Level_1\\Task_17\\input.txt", "r") as f:
    # Setting all 
    lines = 0
    words = 0
    chars = 0
    vowels = 0
    # Triple nested loop very inefficient O(N^3)
    for line in f:
        lines += 1
        # Creating list of words
        word = line.split()
        # Iterating over words in line
        for word in word:
            if word.isalpha():
                words += 1
            # Iterating over char in each word
            for char in word:
                # Check done to see if part of the alphabet
                if char.isalpha():
                    chars += 1
                if char in "aeiou":
                    vowels += 1
    # Printing each value
    print(f"Lines: {lines}")
    print(f"Words: {words}")
    print(f"Char: {chars}")
    print(f"Vowels: {vowels}")

# Same without inefficient 3 nested loops. Only one loop used            
with open(f"{os.getcwd()}\\Level_1\\Task_17\\input.txt", "r") as f:
    lines = 0
    words = 0
    chars = 0
    vowels = 0
    for line in f:
        # Adding 1 to lines with each line iterate
        lines += 1
        # Creating a list of the words of each line and getting the length using list comprehension
        words += len([i for i in line.split() if i.isalpha()])
        chars += len([i for i in line if i.isalpha()])
        vowels += len([i for i in line if i in "aeiou"])
    print(f"Lines: {lines}")
    print(f"Words: {words}")
    print(f"Char: {chars}")
    print(f"Vowels: {vowels}")
