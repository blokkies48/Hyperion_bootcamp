arr = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
TARGET = 9
# Point 1
# Linear search will most likely be ok here
# because it is a small list and it is unsorted 

# Point 2
# I will return the index
def linear_search(arr: list, target: int):
    for index, number in enumerate(arr):
        if number == target:
            return index
# This is a good choice because
# Simple and it is a unsorted array and 
# A very tiny array

print("Linear search on unsorted array ", linear_search(arr, TARGET))
# Point 3
# Sources https://www.youtube.com/watch?v=R_wDA-PmGE4
def insertion_sort(arr: list):
    for j in range(1, len(arr)):
        # Check if the left is bigger than the current item
        # Then a swap is done 
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1] 
            j -= 1 

    

insertion_sort(arr)
print("Proof array is sorted",arr)
# Point 4
# other method of sorting is binary_search.
# A real word example can be to find a ID number 
# Out of thousands of customers or products
# ID numbers tend to be or contain ints and is sorted


# This will return the index in a sorted list
def binary_search(arr: list, target: int):
    left = 0 # Setting beginning of list
    right = len(arr) - 1 # Setting right to end of list

    while left <= right: # looping while till number is found
        mid = (right + left) // 2 
        if arr[mid] == target: # if mid at index = target then  mid will be returned
            return mid
        elif arr[mid] < target: # if number at mid index is smaller than target
            left = mid + 1 # left will be mid plus 1. This example left will be 3
        else:
            right = mid - 1 # Same with the opposite. right will be 1
    return -1 # If element not in list then -1 will be returned
    
print("Binary search sorted array ", binary_search(arr, TARGET))
# I think this is a good choice because it is a lot faster than linear search especially if there is a lot of numbers involved