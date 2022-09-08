
#Declaring string variable
hero = "Super Man"

#Printing hero string with ^ inbetween letters using replace() and making it all caps.
print((hero[0] + hero[1:4].replace("", "^") + hero[4:7] + hero[7:8].replace("", "^") + hero[-1]).upper())
