# Func for working out the total cost for all nights
def hotel_cost(nights):
    return nights * 200 # Returning the amount of nights times cost per night

# Func for plane cost according to question requirement
def plane_cost(city):
    # Each city has a corresponding number
    if city == "Melbourne":
        return 2000
    elif city == "Osaka":
        return 3000
    elif city == "Amsterdam":
        return 4000
    # if no city is found then 0 is returned to avoid crashes in arithmetic
    # you can do a if statement to check this and return something like (city not available) then ask the user again with a while loop
    else:
        return 0

# Car rental func
def car_rental(days):
    return days * 200 # Returns the amount of days times the amount it cost each day

# Holiday total cost func
def holiday_cost(hotel,city,car):
    return hotel + city + car # Simply returns the sum of all the parameters given

# Getting input from user and passing it to each func
hotel_c = hotel_cost(int(input("How many nights are you staying? ")))
plane_c = plane_cost(input("Please select a city.\n1. Melbourne\n2. Osaka\n3. Amsterdam\n:").capitalize())
car_c = car_rental(int(input("For how many days will you need a car? ")))

# Neat way of displaying each detail and having the holiday_cost func in a f string
print(f"Your hotel cost is R{hotel_c:.2f}\nYour plane cost is R{plane_c:.2f}\nYour car rental cost is R{car_c:.2f}\nThe total cost of your holiday will be R{holiday_cost(hotel_c,plane_c,car_c):.2f}")