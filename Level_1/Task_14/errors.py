# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

#No parentheses (SyntaxError)
print ("Welcome to the error program")
#Indent errors and missing parentheses (IndentError/ Syntax Error)
print( "\n")

#Comperason operator not equal to (Syntax Error/NameError)
ageStr = "24 years old"
#Trying to convert string to int(ValueError/ Runtime Error)
#age should be just 24 (Logical Error)
age = 24
#No spaces after I'm and before years(Logical Error)
#Can't concatenate string(TypeError/Runtime Error)
print("I'm " + str(age) + " years old.")
#The variable should be a int and .5 should be added for the 6 monthd(Logical Error)
three = 3.5

answerYears = age + three
#No parentheses and qoute marks around variable(Syntax Error)
#Space after years(Logical Error)
#Can't add int to string(Runtime Error)
#Should be age not answerYears (Logical Error)
print ("The total number of years: " + str(age))
#Missing rest of answerYears(Logical Error/NameError)
#answerMonths is strings so won't work(Logical Error)
answerMonths = answerYears * 12
#Can't add int to string (Runtime Error)
#Set answerMonths to int to drop the .0 when printing(Logical Error)
print ("In 3 years and 6 months, I'll be " + str(int(answerMonths)) + " months old")

#HINT, 330 months is the correct answer

