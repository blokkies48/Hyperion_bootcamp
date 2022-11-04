#Setting string variable
str1 = "Hello World"

#Initiating count variable
i = 0
#Setting a empty list
str_lst = []
for letter in str1:
    #Checking if the letter index is even to set it to upper and append to list
    if i % 2 == 0:
        str_lst.append(letter.upper())
    #Else if letter index is odd. Set it to lower and appending to list
    else:
        str_lst.append(letter.lower())
    #Increasing count by one
    i += 1

#Printing the list in a joint string
print("".join(str_lst)) 