#Importing date from datetime module
from datetime import date

#Getting current year from datetime and storing it in a variable
#Asking user for birth year and converting it to an int
current_year = date.today().year
birth_year_of_user = int(input("Please enter your birth year: "))

#Basic mach arithmetic to get age from input and current year
age_of_user = current_year - birth_year_of_user

#Checking if the age of user is equal or greater than 18
if age_of_user >= 18:
    print("Congrats you are old enough")