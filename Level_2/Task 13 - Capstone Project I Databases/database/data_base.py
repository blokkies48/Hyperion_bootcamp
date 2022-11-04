# This file is used to create the database
from database.populate_database import *
import os
import sqlite3


# Database objects
db = sqlite3.connect("ebookstore.db")
cursor = db.cursor()

# Creates initial table in database
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books 
    (
    Id INTEGER PRIMARY KEY, 
    Title TEXT, 
    Author TEXT, 
    Qty INTEGER
    )
    ''') 

# Side note: This block most likely won't be needed in real world programmes
# Because real world the database will most likely be created with the programme or another.
# Run this code only once with the initial starting program to build initial database create a file to check than when programme start again the file will be there and code won't run
if not os.path.isfile("first_time\\first_time_done.txt"):
    cursor.executemany("INSERT INTO books VALUES (?,?,?,?)", books)
# Creates file to check against
with open("first_time\\first_time_done.txt", "w") as first:
    first.write("File used to check if this is the first time the programme ran")
# If there is a better way to do this then please let me know. 
# I found that there was crashes if I made changes in the database then run the program again. 
# That is why this is needed


# Committing updates
db.commit()

###
# Note: Why this file will be needed with every launch is due to the database objects needed in the rest of the code.

# //Sources//
# https://www.geeksforgeeks.org/python-check-if-a-file-or-directory-exists/:~:text=isdir()%20Method%20to%20check,an%20existing%20directory%20or%20not