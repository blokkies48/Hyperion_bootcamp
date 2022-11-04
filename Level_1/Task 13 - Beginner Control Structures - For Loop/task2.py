#Asking user for inputs
year = int(input("Please enter a year: "))
num_of_years = int(input("How many years do you want to check: "))

#Looping over in the range of years 
## 1 and + 1 isn't used because num_of_years is only used as a counter
for i in range(num_of_years):
    #Checking for leap year of not
    if year % 4 == 0:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} isn't a leap year.")
    #Increasing the year by 1 to check the following year
    year += 1

