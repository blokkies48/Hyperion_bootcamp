#Creating a menu using string and setting it to a variable.
menu = "\n---Welcome to FoodPlace---\n\tMENU\n1. Chicken nuggets\n2. Hamburger\n3. Chickenburger\n4. Fish and chips\n5. Steak and chips\n6. Schnitzel\n7. Spaghetti bolognaise"

#Print menu to the console.
print(menu+"\n")

#Asking user for their 3 favourite items.
print("Please order 3 of your favourite items. (Write out the full names)\n")
item_1 = input("Enter your first favourite item's name: ")
item_2 = input("\nEnter your second favourite item's name: ")
item_3 = input("\nEnter your third favourite item's name: ")

#Prints out the items the user chose
print("\nYour oder is:")
print(f"\n{item_1}\n{item_2}\n{item_3}\n")

