# Base case of this problem will be just to sum index 0

# With each loop you will have to add the number at the index to the pervious number(right)
# Then subtract 1 from the index input number
# Return the result
# 
# 

def sum_recursion(lst_p, index):
    lst = list(lst_p) # Setting list 2 to be a instance of list passed to avoid modifying the list
    index -= 1 # Reducing index by one with each loop
    sum = lst[0] # Setting sum to equal the first index
    lst[index] = lst[index + 1] + lst[index] # Modifying the list so the num at the index equals it plus the number at its left
    if index == -1: return sum # Returning the sum if index is - 1 because that indicates we went over all the numbers in a list
    else: return sum_recursion(lst, index) # Returning the function with the modified list and index

list_1 = [1,4,5,3,12,16]

print(sum_recursion(list_1,4))
print(sum_recursion([4,3,1,5],1))

# print(list_1) # Proof list isn't modified