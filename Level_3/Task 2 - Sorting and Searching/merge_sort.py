# Get the random words to pass into the list.
# Made this for the fun of it to practice a bit
from random import randint

def random_list_10_words():
    return_list = [] 
    
    random_list_int = [randint(0,999) for _ in range(10)]
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
    items = [len(string) for string in str_list] 
    arr_len = len(items)
    temporary_storage = [None] * arr_len
    size_of_subsections = 1
    while size_of_subsections < arr_len:
        for i in range(0, arr_len, size_of_subsections * 2):
            i1_start, i1_end = i, min(i + size_of_subsections, arr_len)
            i2_start, i2_end = i1_end, min(i1_end + size_of_subsections, arr_len)
            sections = (i1_start, i1_end), (i2_start, i2_end)
            merge(items, sections, temporary_storage)
        size_of_subsections *= 2

    # Best way I could come up with
    # Add another section to the algorithm
    # New placeholder list created to empty to avoid duplication
    # Checks sorted int list to the string list
    placeholder = list(str_list)
    for index, number in enumerate(items):
        for string in placeholder:
            if len(string) == number:
                # Removes the string from the list to avoid duplication
                placeholder.remove(string)
                str_list[index] = string
                break # Break if first match is satisfied
    return str_list[::-1] # Returns descending order

# Code gotten from notes
def merge(items, sections, temporary_storage):
    (start_1, end_1), (start_2, end_2) = sections
    int_1 = start_1
    int_2 = start_2
    int_t = 0
    while int_1 < end_1 or int_2 < end_2:
        if int_1 < end_1 and int_2 < end_2:
            if items[int_1] < items[int_2]:
                temporary_storage[int_t] = items[int_1]
                int_1 += 1
            else: # the_list[int_2] >= items[int_1]
                temporary_storage[int_t] = items[int_2]
                int_2 += 1
            int_t += 1
        elif int_1 < end_1:
            for i in range(int_1, end_1):
                temporary_storage[int_t] = items[int_1]
                int_1 += 1    
                int_t += 1
        else: # int_2 < end_2
            for i in range(int_2, end_2):
                temporary_storage[int_t] = items[int_2]
                int_2 += 1
                int_t += 1
    for i in range(int_t):
        items[start_1 + i] = temporary_storage[i]
        

'''Test cases'''
# Random words gotten from https://www.randomlists.com/random-words
for _ in range(3): # Loop to generate test cases
    list_1 = random_list_10_words()
    print(f"\nUnsorted list: {list_1}")
    print(f"Sorted list: {merge_sort(list_1)}")
    print("Proof: ", [len(item) for item in merge_sort(list_1)], "\n") # For proof list is sorted
    