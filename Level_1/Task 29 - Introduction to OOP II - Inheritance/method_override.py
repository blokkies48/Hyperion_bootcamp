class Adult():
    def __init__(self, name, age, eye_colour, hair_colour):
        self.name = name
        self.age = age
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour
    
    def can_drive(self):
        # If age is 18 or older 
        print(f"{self.name} can drive because they are old enough")
            

class Child(Adult):
    def __init__(self, name, age, eye_colour, hair_colour):
        super().__init__(name, age, eye_colour, hair_colour)

    def can_drive(self): # Overriding the method
        print(f"{self.name} can't dive! Because they are too young.")




def main():
    # Asking user for info on the person
    name = input("Enter your name: ")
    age = int(input("Enter you age: "))
    eye_colour = input("Enter your eye colour: ")
    hair_colour = input("Enter your hair colour: ")

    # Logic done to check the age
    if age > 17:
        adult = Adult(name = name, eye_colour = eye_colour,age = age, hair_colour = hair_colour) # Using keyword args to not get confused and for practice
        adult.can_drive() # Calling can drive method
    else:
        child = Child(name = name, eye_colour = eye_colour,age = age, hair_colour = hair_colour)
        child.can_drive()



main() # Calling on main method to run code