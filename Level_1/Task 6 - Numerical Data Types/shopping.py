#Stings to avoid repetition
ask_name = "Please enter the name of the {} product: "
ask_price = "Please enter the price of the {} product: "

#Asks for the names of the products
products = input(ask_name.format("1st")),input(ask_name.format("2nd")),input(ask_name.format("3rd"))

#Asks for the price of the products
price_products = float(input(ask_price.format("1st"))),float(input(ask_price.format("2nd"))),float(input(ask_price.format("3rdw")))

#Calculating the price and total of the products
#Using total to the calculate the average
#Rounding both to 2 decimal place
total_price = round(sum(price_products),2)
average_price = round(total_price/len(price_products),2)

#Printing out string required
print(f"The total of {products[0]}, {products[1]}, {products[2]} is R{total_price} and the average price of the items is R{average_price}")