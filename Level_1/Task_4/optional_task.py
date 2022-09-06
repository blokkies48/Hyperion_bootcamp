#Get 2 numbers from user and storing values in a tuple
num1, num2 = int(input("Input first number: ")), int(input("Input second number: "))
##(Note) You can put tuple1 instead of num1, num2 to shorten the code even more. But the question asks for storing in separate variables.
tuple1 = num1, num2

#Swapping the numbers' values and storing them in another tuple
num2, num1 = tuple1
tuple2 = num1,num2

##(Note)tuple2 = tuple1[1] , tuple1[0] You can use indexing as well to completely get rid of storing a lot of variables especially in larger code

#Printing values of num1 and num2 befor and after swapping
#I chose tuple because you will always have the original order if you might need it later.
print("Values before swapping are " + str(tuple1))
print("Values after swapping are " + str(tuple2))

#Another way you can print without using tuple
print(f"Values before swapping are {num2} and {num1} " )
print(f"Values after swapping are {num1} and {num2}" )
