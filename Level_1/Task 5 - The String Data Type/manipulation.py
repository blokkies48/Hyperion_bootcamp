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

#Printing each letter to a new line
print(str_manip.replace(" ","\n"))

##Reviewer said letter and question said word not sure what. Question isn't detailed enough I though it ment print out all previous words created on a new line
### Not sure if we are suposed to use for loops because it hasn't been covered yet

#Printing out each letter
for letter in str_manip:
    if letter != " ":
        print(letter)
    