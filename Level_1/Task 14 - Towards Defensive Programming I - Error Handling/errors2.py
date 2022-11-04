# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

#Not qoute marks(Syntax error)
animal = "Lion"
animal_type = "cub"
number_of_teeth = 16

#No f string (Logic Error)
#Number of teeth and animal type is swapped(Logic Error)
full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"

#No parentheses (Syntax Error)
print (full_spec)

