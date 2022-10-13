# This file contains all the logical operations functions

from database.data_base import *

DICT_OF_OPERATIONS = {1:"Id", 2:"Title", 3:"Author", 4:"Qty"}

# Printing the table
def print_table():
    for book in cursor.execute("SELECT * FROM ebookstore"):
        print(book)

def add_book():
    # Two loops used to reduce retyping if user makes a mistake
    while True:
        try:
            id = int(input("Enter id: "))
            qty = int(input("Enter qty: "))
            break
        except ValueError:
            print("Enter correct id please!")
    while True:
        title = input("Title: ")    
        author = input("Author: ")
        break

    new_book = Book(Id=id, Title=title, Author=author, Qty= qty)
    cursor.execute("INSERT INTO ebookstore VALUES (?,?,?,?)",new_book.add_to_db())
    
# Updates books where 
def update_info():
    print("What do you want to update?")
    val = find_what_to_use()
    print(f"What is the {DICT_OF_OPERATIONS[val]} you want to change to")
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
    if val == 1:
        cursor.execute("UPDATE ebookstore SET Id = ? WHERE Id = ?", (new_value,old_value))
    if val == 2:
        cursor.execute("UPDATE ebookstore SET Title = ? WHERE Title = ?", (new_value,old_value))
    if val == 3:
        cursor.execute("UPDATE ebookstore SET Author = ? WHERE Author = ?", (new_value,old_value))
    if val == 4:
        cursor.execute("UPDATE ebookstore SET Qty = ? WHERE Qty = ?", (new_value,old_value))

# Deletes book according to the id of the book
def delete_book():
    while True:
        try:
            id_of_book = int(input("Enter id of book you want to delete: "))
            break
        except ValueError:
            print("Enter a valid id")
    cursor.execute("DELETE FROM ebookstore WHERE Id = ?", (id_of_book,))      

# Searching for a book 
def search_book():
    # Same logic used in update
    print("What do you want to search by?")
    val = find_what_to_use()
    print(f"What is the {DICT_OF_OPERATIONS[val]} you want to find?")
    while True:
        try: 
            search_val = input("Enter search: ")
            if val == 1 or val == 4:
                search_val = int(search_val)
            break
        except ValueError:
            print("Enter a valid search value")
    if val == 1:
        cursor.execute("SELECT * FROM ebookstore WHERE Id = ?", (search_val,))
    if val == 2:
        cursor.execute("SELECT * FROM ebookstore WHERE Title = ?", (search_val,))
    if val == 3:
        cursor.execute("SELECT * FROM ebookstore WHERE Author = ?", (search_val,))
    if val == 4:
        cursor.execute("SELECT * FROM ebookstore WHERE Qty = ?", (search_val,))

# Duplicate code used in search and update_info
def find_what_to_use():
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
        
