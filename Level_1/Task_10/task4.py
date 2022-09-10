#Asking for a integer
num = int(input("Please enter a whole number.\n"))

#Doing checks on the number given
if num % 2 == 0 and num % 5 == 0:
    print("Number is divisible by 2 and 5.")
#Use elif because if you use another if you will get both outputs for number 10 for example. 
elif num % 2 == 0 or num % 5 == 0:
    print("Number is divisible by 2 or 5.")
#No need for another check because all numbers that don't meet above criteria will reult in this.
else:
    print("Not divisible by 2 or 5")