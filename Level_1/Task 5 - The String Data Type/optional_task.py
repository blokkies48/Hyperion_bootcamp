#Asking user to input favourite restaurant
fav_rest = input("What is your favourite restaurant? ")
#Asking user for their favourite number and casting it to an int
int_fav = int(input("What is your favourite number? "))

#Printing both fav_rest and int_fav
print(fav_rest)
print(int_fav)

#Attempting to cast a string as an integer
int_rest = int(fav_rest)

'''
ValueError exeption was raised due to string not being in base 10 value.

This happens when a letter or character that isn't in the base 10 range is tried to be casted to base 10. eg. Ones, Tens, Hunderds, and so on.

Note: floats will also give a ValueError.
'''