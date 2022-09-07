# Getting a sentence from the user
str_manip = input("Please enter a sentence: ")

#Printing the length of the string
print(len(str_manip))

#Printing the sentence with the @ in every position where the last letter occurs
print(str_manip.replace(str_manip[-1],"@"))

#Getting the last 3 letters and printing them in reverse
print(str_manip[-1:-4:-1])


#Getting the first 3 letters and last 2 and printing them
print(str_manip[0:3] + str_manip[-2:])
