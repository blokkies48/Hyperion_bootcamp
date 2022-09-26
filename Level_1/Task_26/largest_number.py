# Breaking down the problem 
# Must compare the next number to the largest/current number
# Set current to largest
# If current number is bigger than the next number pass
# If the next number is bigger than current set the next to largest/current

# The base case will be if the list has 1 int in

def largest_number(lst):
    largest_num = lst[0] # Setting first num in list to largest
    if len(lst) == 1: # If list only has one item in then return that item
        return largest_num
    elif largest_num <= lst[1]: # Checking if second number is larger than the first number
        largest_num = lst[1] # Setting larger number to that item
        lst.pop(0) # Removing the first item
        return largest_number(lst) # Returning the function
    else: # If number isn't larger then remove that number
        lst.pop(1)
        return largest_number(lst) # Returning the function with the modified list


print(largest_number([1,4,5,3]))
print(largest_number([3,1,6,8,2,4,5]))