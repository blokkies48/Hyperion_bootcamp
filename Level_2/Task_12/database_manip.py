import sqlite3 
from random import randint

# Creating the file and cursor object
db = sqlite3.connect("python_programming.db")
cursor = db.cursor()

# Creating the table
cursor.execute('''
    CREATE TABLE python_programming
    (
    id INTEGER PRIMARY KEY,
    name TEXT, 
    grade INTEGER
    )

''')
# Creating the rows for the database
rows = [
    (55,"Carl Davis", 61),
    (66,"Dennis Fredrickson", 88),
    (77,"Jane Richards", 78),
    (12,"Peyton Sawyer", 45),
    (2,"Lucas Brooke", 99),
]

# Adding the rows in the database
cursor.executemany("INSERT INTO python_programming VALUES(?,?,?)", rows)

# Showing all rows to check if data is correct
print("\nAll rows")
for row in cursor.execute("SELECT * FROM python_programming"):
    print(row)

# Printing all the rows that meet the criteria
print("\nAll rows where grade is between 60 and 80")
for row in cursor.execute("SELECT * FROM python_programming WHERE grade > 60 AND grade < 80"):
    print(row)

# Changing the grade of Carl Davis
cursor.execute("UPDATE python_programming SET grade = 65 WHERE name = 'Carl Davis'")

# Deleting the row where bane is Dennis Fredrickson
cursor.execute("DELETE FROM python_programming WHERE name = 'Dennis Fredrickson'")

# Changing grades of people with id lower than 55.
cursor.execute("UPDATE python_programming SET grade = 99 WHERE id < 55")

# Checking if changes took place
print("\nAll rows after updates")
for row in cursor.execute("SELECT * FROM python_programming"):
    print(row)

# To save edits on database
db.commit()
