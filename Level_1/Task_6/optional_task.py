#Asks user for the 3 sides of a triangle
print("\nPlease enter the three sides of and triangle")
sides = float(input("1st side ")),float(input("2nd side ")),float(input("3rd side "))

#Set s to reuse in formula
#Calculating area using Heron's formula
s = sum(sides)/2
area_of_triangle = round((s*(s-sides[0])*(s-sides[1])*(s-sides[2]))**0.5,4)
#Printing to console.
print(area_of_triangle)
