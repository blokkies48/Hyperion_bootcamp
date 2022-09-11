#Initiat names before loop else with every loop names is set to an empty list
names = []

#Initialing loop to true
while True:
    #With every iteration ask for a input
    name_entered = input("Please enter a name of a student or enter stop to finish\n:")
    
    #If stop is entered loop will be broken
    if name_entered.upper() == "STOP":
        break
    #Any string entered will be added to a list
    else:
        names.append(name_entered)

#Print the length of names list after breaking loop
print(len(names))


'''
#Whitout if statment
#Initiating name entered to an empty string to do check
name_entered = ""

#Initiating while loop with condition
while name_entered.upper() != "STOP":
    name_entered = input("Please enter a name of a student or enter stop to finish\n:")
    names.append(name_entered)

#Has to pop last item because last item will be stop
names.pop()
print(len(names))
'''
