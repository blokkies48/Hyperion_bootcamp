# This file contains all the logical operations functions

from database.data_base import *
# Setting constant dictionary for referencing
DICT_OF_OPERATIONS = {1:"Id", 2:"Title", 3:"Author", 4:"Qty"}

# Printing the table
def print_table():
    for book in cursor.execute("SELECT * FROM books"):
        print(book)

# Logic to add book to the database
def add_book():
    # Logic for user input
    while True:
        try:
            id = int(input("Enter id: "))
            qty = int(input("Enter qty: "))
            break
        except ValueError:
            print("Enter correct value please!")
    
    title = input("Title: ")    
    author = input("Author: ")
        
    # Creating new book object and adding it to the database
    new_book = Book(Id=id, Title=title, Author=author, Qty= qty)
    cursor.execute("INSERT INTO books VALUES (?,?,?,?)",new_book.add_to_db())
    
# Updates books where 
def update_info():
    # Handling user input logic
    print("What do you want to update?")
    val = find_what_to_use() # Calling function that is reused
    print(f"What is the {DICT_OF_OPERATIONS[val]} you want to change to") # Getting value from dictionary
    # Logic for user inout getting new and old values to replace
    while True:
        old_value = input("Old value: ")
        new_value = input("New Value: ")
        if val == 1 or val == 4:
            try:
                new_value = int(new_value)
                old_value = int(old_value)
                break
            except ValueError:
                print("Invalid value")
        else:
            break
    # Updating to the database relevant to the user's choices
    if val == 1:
        cursor.execute("UPDATE books SET Id = ? WHERE Id = ?", (new_value,old_value))
    if val == 2:
        cursor.execute("UPDATE books SET Title = ? WHERE Title = ?", (new_value,old_value))
    if val == 3:
        cursor.execute("UPDATE books SET Author = ? WHERE Author = ?", (new_value,old_value))
    if val == 4:
        cursor.execute("UPDATE books SET Qty = ? WHERE Qty = ?", (new_value,old_value))

# Deletes book according to the id of the book
def delete_book():
    # Logic to handle user input
    while True:
        try:
            id_of_book = int(input("Enter id of book you want to delete: "))
            break
        except ValueError:
            print("Enter a valid id")
    # Deleting book from table
    cursor.execute("DELETE FROM books WHERE Id = ?", (id_of_book,))      

# Searching for a book 
def search_book():
    # Same logic used in update
    print("What do you want to search by?")
    val = find_what_to_use()
    print(f"What is the {DICT_OF_OPERATIONS[val]} you want to find?")
    # User logic to get what they are searching for
    while True:
        try: 
            search_val = input("Enter search: ")
            # This done because column 1 and 4 are integers
            if val == 1 or val == 4:
                search_val = int(search_val)
            break
        except ValueError:
            print("Enter a valid search value")
    
    book_found = False # Book isn't found at first
    # Logic done relevant to the user input
    if val == 1:
        # Logic the same for other choices
        # Looping over the relevant items in the database
        for i in cursor.execute("SELECT * FROM books WHERE Id = ?", (search_val,)):
            # Printing the book to the console 
            print("Your book")
            print(f"--{i}--")
            book_found = True # Setting book found to true
    elif val == 2:
        for i in cursor.execute("SELECT * FROM books WHERE Title = ?", (search_val,)):
            print("Your book")
            print(f"--{i}--")
            book_found = True
    elif val == 3:
        for i in cursor.execute("SELECT * FROM books WHERE Author = ?", (search_val,)):
            print("Your book")
            print(f"--{i}--")
            book_found = True
    elif val == 4:
        for i in cursor.execute("SELECT * FROM books WHERE Qty = ?", (search_val,)):
            print("Your book")
            print(f"--{i}--")
            book_found = True

    # IF book not found
    if not book_found:
        print("--There isn't a book matching the search--")
    

# Duplicate code used in search and update_info
def find_what_to_use():
    # Just logic for what is the column they want
    print("1. ID\n2. Title\n3. Author\n4. Qty")
    while True:
        try:
            val = int(input(": "))
            if val in range(1,5):
                break
            else:
                print("Enter a value from 1 to 4")
        except ValueError:
            print("Enter a value from 1 to 4") 
    return val
        
