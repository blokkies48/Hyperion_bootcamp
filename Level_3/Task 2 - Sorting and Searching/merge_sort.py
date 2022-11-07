# Get the random words to pass into the list.
# Made this for the fun of it to practice a bit
from random import randint

def random_list_10_words():
    return_list = [] # The list that will be returned
    # List of random ints to use to get the random words
    random_list_int = [randint(0,999) for i in range(10)]
    # Reading the words from the file
    with open("1000_random_words.txt", "r") as f:
        for index, line in enumerate(f):
            if index in random_list_int and len(return_list) <= 10:
                return_list.append(line.strip("\n"))
    return return_list

'''Merge sort algorithm'''
# Algorithm gotten from the notes😃
def merge_sort(str_list):
    # Changing the list strings to ints
    items = [len(i) for i in str_list] 
    n = len(items)
    temporary_storage = [None] * n
    size_of_subsections = 1
    while size_of_subsections < n:
        for i in range(0, n, size_of_subsections * 2):
            i1_start, i1_end = i, min(i + size_of_subsections, n)
            i2_start, i2_end = i1_end, min(i1_end + size_of_subsections, n)
            sections = (i1_start, i1_end), (i2_start, i2_end)
            merge(items, sections, temporary_storage)
        size_of_subsections *= 2

    # Best way I could come up with
    # Add another section to the algorithm
    # New placeholder list created to empty to avoid duplication
    # Checks sorted int list to the string list
    placeholder = list(str_list)
    # Loops over the sorted int list with enumerate
    for index, number in enumerate(items):
        # Then loops over the placeholder list
        for string in placeholder:
            # Checks the length of the string to the number in the int list
            if len(string) == number:
                # Removes the string from the list to avoid duplication
                placeholder.remove(string)
                # Replaced the string at the index
                str_list[index] = string
                break # Break if first match is satisfied
    # Returns the modified original list
    return str_list[::-1] # Returns descending order


def merge(items, sections, temporary_storage):
    (start_1, end_1), (start_2, end_2) = sections
    i_1 = start_1
    i_2 = start_2
    i_t = 0
    while i_1 < end_1 or i_2 < end_2:
        if i_1 < end_1 and i_2 < end_2:
            if items[i_1] < items[i_2]:
                temporary_storage[i_t] = items[i_1]
                i_1 += 1
            else: # the_list[i_2] >= items[i_1]
                temporary_storage[i_t] = items[i_2]
                i_2 += 1
            i_t += 1
        elif i_1 < end_1:
            for i in range(i_1, end_1):
                temporary_storage[i_t] = items[i_1]
                i_1 += 1    
                i_t += 1
        else: # i_2 < end_2
            for i in range(i_2, end_2):
                temporary_storage[i_t] = items[i_2]
                i_2 += 1
                i_t += 1
    for i in range(i_t):
        items[start_1 + i] = temporary_storage[i]
        

'''Test cases'''
# Random words gotten from https://www.randomlists.com/random-words
for _ in range(3): # Loop to generate test cases
    list_1 = random_list_10_words()
    print(f"\nUnsorted list: {list_1}")
    print(f"Sorted list: {merge_sort(list_1)}")
    print("Proof: ", [len(i) for i in merge_sort(list_1)], "\n") # For proof list is sorted
    