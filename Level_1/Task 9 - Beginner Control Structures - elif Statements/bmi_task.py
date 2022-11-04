#Asking user for weight and height
weight = float(input("Please enter weight in kg: "))
height = float(input("Please enter your height in meters: "))

#Formula for BMI
BMI_user = weight/height**2

#Printing status using conditional statements and BMI score.
if BMI_user >= 30:
    print("Obese")
elif BMI_user >= 25:
    print("Overweight")
elif BMI_user >= 18.5:
    print("Normal")
else:
    print("Underweight")


