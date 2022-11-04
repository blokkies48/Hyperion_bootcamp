"""
Compulsory Task 1: 
------------------

Use the code provided copied to a new file named compulsory_task_1.py: 
1. Add another method in the Course class that prints the head office location: Woodstock, Cape Town
2. Create a subclass of the Course class named OOPCourse
3. Create a constructor that initializes the following attributes and assigns these values:
    --- "description" with a value "OOP Fundamentals"
    --- "trainer" with a value "Mr Anon A. Mouse"
4. Create a method in the subclass named "trainer_details" that prints what the 
   course is about and the name of the trainer by using the description and trainer attributes.
5. Create a method in the subclass named "show_course_id" that prints the ID number of the course: #12345
6. Create an object of the subclass called course_1 and call the following methods
   contact_details
   trainer_details
   show_course_id
   These methods should all print out the correct information to the terminal

On a side note, this task covers single inheritance. multiple inheritance is also possible in Python and 
we encourage you to do some research on multiple inheritance when you have finished this course
"""
class Course: # The parent class without any constructor
    # Defining variables
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"
    head_office_location = "Woodstock, Cape Town"

    # Two methods that are required by the task
    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    def head_office(self):
        print(f"The head office is currently located at {self.head_office_location}")

    
# Creating the OOPCourse class that inherence from the Course class
class OOPCourse(Course):
    # Setting variable in a constructor 
    def __init__(self):
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"
        self.id = "12345" # Creating ID variable to use in method
    
        # No need for super because there is no constructor in the parent

    # Two methods created for the task 
    # Both are printing f strings with the variable passed to it
    def trainer_details(self):
        print(f"The course is about {self.description}.\nThe trainer is {self.trainer}.")

    def show_course_id(self):
        print(f"The course id is {self.id}")


def main(): # The main method will indicate the code that has to be ran

    course_1 = OOPCourse() # Creating an object of the OOPCourse class

    # Calling on the methods as required in the task
    course_1.contact_details()
    course_1.trainer_details()
    course_1.show_course_id()

main() # Calling the main method to run