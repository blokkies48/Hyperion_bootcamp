from random import randint

# Generating a random board just ofr fun
def random_grid(bombs):
    if 0 > bombs or bombs > 24: # Used to raise exception if out of range
        raise Exception
    grid = [ 
            ["-","-","-","-","-"],
            ["-","-","-","-","-"],
            ["-","-","-","-","-"],
            ["-","-","-","-","-"],
            ["-","-","-","-","-"] 
            ] # Setting a empty grid


    for _ in range(bombs): # Looping over in the range of bombs passed
        while True: # To make sure bomb is placed
            x,y = randint(0,4),randint(0,4) # Getting random coordinates
            if grid[x][y] != "#": # To avoid place bomb over other bomb
                grid[x][y] ="#" # Setting random positions to bombs in grid
                break
    
    return grid # Returning random grid


def find_mines(grid):
    # Getting the positions of each bomb and not bomb
    list_index_1 = []
    list_index_2 = []
    num_position_1 = []
    num_position_2 = []
    # Getting the indexes and saving them to a list of tuples
    for index, line in enumerate(grid):
        for index2, item in enumerate(line):
            if item == "#": # Getting positions of the bombs
                list_index_1.append(index)
                list_index_2.append(index2)
                positions_tup_bomb = list(zip(list_index_1,list_index_2)) # Zipping them together into a list. Done for both
            if item == "-": # Getting positions where there isn't bombs
                num_position_1.append(index)
                num_position_2.append(index2)
                num_pos_tup = list(zip(num_position_1,num_position_2))

    # Comparing the two positions that where collected 
    for tup in num_pos_tup: # Looping over the list of positions without bombs
        num_at_pos = 0 # Setting the number to 0
        # Looping over positions with the bombs to compare each non bomb position to each bomb position
        for tup2 in positions_tup_bomb: 
            '''
            # Comparisons done by taking the non bomb pos and seeing if the bomb pos is either + 1, - 1 with x which is row and y which is column
            first the rows are checked with - 1 and + 1 to find if a bomb is next to the pos in the next or previous rows
            In the same line it is also checked that it is in the same column or in a column next to it
            Next in the columns are checked this is simpler because across has already been checked
            '''
            if tup[0] == tup2[0] -1 and (tup[1] == tup2[1] -1 or tup[1] == tup2[1] + 1 or tup[1] == tup2[1]): 
                num_at_pos += 1
            if tup[0] == tup2[0] + 1 and (tup[1] == tup2[1] -1 or tup[1] == tup2[1] + 1 or tup[1] == tup2[1]):
                num_at_pos += 1
            if tup[0] == tup2[0] and tup[1] == tup2[1] - 1 and tup2[1] - 1 > -1: # Here another condition has to be met so that it doesn't check the last line because index of -1 is the last item
                num_at_pos += 1
            if tup[0] == tup2[0] and tup[1] == tup2[1] + 1:
                num_at_pos += 1
        
        grid[tup[0]][tup[1]] = str(num_at_pos)  # Setting the given position to the number at that position and setting to string

    # Printing out the board in a neat manner
    for line in grid:
        print(line)


# The grid passed to the function
grid_of_mines = [ 
                ["-","-","-","#","#"],
                ["-","#","-","-","-"],
                ["-","-","#","-","-"],
                ["-","#","#","-","-"],
                ["-","-","-","-","-"] 
                ]
# Calling on find mines function
find_mines(grid_of_mines)
print() # Just to add space in console
# Another one to see that code is dynamic
try:
    find_mines(random_grid(int(input("How many bombs to you want? 1 to 24: ")))) # Getting random grid passing it to find mines and asking user for how many bombs do they want in a range 
except: # If exception was raised
    print("Number entered is out of range!")