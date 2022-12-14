
#While loop used to keep asking till user has entered thier name
while True:
    #Asking user for thier name and storing it
    user_names = input("Please enter you full name and surname: ")
    #Checking if user entered anything
    if user_names == "":
        print("You haven't entered anything Please enter you full name.")
    #Checking if user entry is more than 3 characters long
    elif len(user_names) < 4:
        print("You have entered less than 4 characters. Please make sure that you entered your name and surname.")
    #Checking is entry is less than 26 characters 
    elif len(user_names) > 25:
        print("You have entered more than 25 characters. Please make sure that you have only entered you full name.")
    #Added another condition that wasn't in the validation check, but the question does mention to check for at least 2 names.
    #I did this with checking if there is a space in the string
    elif " " not in user_names:
        print("Please enter at least two names or add space between your names") 
    #Printing thank you when none of the conditions are met and also breaking out of the loop
    else:
        print(f"Thank you {user_names}, for entering your name!")
        break