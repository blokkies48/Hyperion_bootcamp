#Asking user for 3 numbers and saving them in a tuple
tup_nums = int(input("Please enter 1st number: ")),int(input("Please enter 2nd number: ")),int(input("Please enter 3rd number: "))

#Displaying the numbers to console for proof
print(tup_nums)

#Using build in funtion to find the sum of all numbers
print(sum(tup_nums))

#Using indexing to do arithmetic operations and printing them
print(tup_nums[0] - tup_nums[1])
print(tup_nums[2] * tup_nums[0])
print(sum(tup_nums)/tup_nums[2])

'''Another bonus to find the sums manually'''
sum1 = 0
for num in tup_nums:
    sum1 += num
print(sum1)