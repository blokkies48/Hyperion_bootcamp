# Lists to store values
menu = ["americana", "latte", "filter", "tea"]
stock_lst = [2, 3, 4, 5]
price_lst = [10.00, 20.00, 5.00, 15.00]
# Dict comprehension from https://www.geeksforgeeks.org/python-convert-two-lists-into-a-dictionary/
# List comprehension used to avoid repeating code
stock = {menu[i] : stock_lst[i] for i in range(len(menu)) }
price = {menu[i] : price_lst[i] for i in range(len(menu)) }

# Value set to zero to start with
value = 0

# Looping over items in the menu to get the keys of each dict
for item in menu:
    # Adding stock value * price value to value 
    value += stock[item] * price[item]
    
# Total value of stock
print(f"R{value:.2f}")