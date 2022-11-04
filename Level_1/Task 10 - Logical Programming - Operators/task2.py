#Importing pi for later use
from math import pi

#Using multiple print statements to just give a more readable output and more readalble code.
print("Please enter the shape of the building (square, rectangular, or round)")
#Getting input and making sure it is all lower
shape = input("Shape: ").lower()

#Comparing input to what shape is required
##Doing arithmetic to figure out area
#Float use because you can get . size
if shape == "square":
    print("What is the length of the square")
    length_square = float(input("Length: "))
    print("Area of the {} shape is {}".format(shape.capitalize(), length_square**2))

elif shape == "rectangular":
    print("What is the length and width of the building")
    length_rec = float(input("Length: "))
    width_rec = float(input("Width: "))
    print("Area the {} shape is {}".format(shape.capitalize(),length_rec * width_rec))

elif shape == "round":
    print("What is the radius of the circle")
    radius_circle = float(input("Radius: "))
    print("Area the {} shape is {}".format(shape.capitalize(),pi * (radius_circle ** 2)))

#If a invalid shap was entered
else:
    print("Sorry you did not input a valid shape.")
