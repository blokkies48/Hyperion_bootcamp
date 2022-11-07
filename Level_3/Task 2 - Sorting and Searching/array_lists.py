class Album(): # Album object
    # The str added to indicate what should be passed to the album object
    def __init__(self, album_name: str, artist_name: str, number_of_songs: int):
        self.album_name = album_name
        self.artist_name = artist_name
        self.number_of_songs = number_of_songs

    # Returning list in a tuple format
    def __str__(self):
         return (self.album_name, self.artist_name, self.number_of_songs)

    

# Creating list of Album objects 
albums1 = []

albums1.append(Album("Jagged Little Pill", "Alanis Morissette", 13))
albums1.append(Album("The Dark Side of the Moon", "Pink Floyd", 10))
albums1.append(Album("21", "Adele", 11))
albums1.append(Album("Rumours", "Fleetwood Mac", 12))
albums1.append(Album("1", "The Beatles", 27))


# Used to get the tuple from the objects😊
str_lst = [i.__str__() for i in albums1]
# Sorting using a lambda method to get the 3rd item
# in the tuple as the key
str_lst.sort(key=lambda x: x[2])
# Printing items sorted in ascending order
print(str_lst)

# Swapping the positions by simply
# Equaling the positions to one another
# Great feature of python 
def swap_positions(albums1):
    albums1[1], albums1[0] = albums1[0], albums1[1]
    return albums1
# Printing the operation of swap_positions
# Using the string list set instead of the object list
print(swap_positions(str_lst))

# Creating the second album list
albums2 = []

albums2.append(Album("Aquemini", "OutKast", 16))
albums2.append(Album("Legend", "Bob Marley and the Wailers", 16))
albums2.append(Album("Ramones", "Ramones", 20))
albums2.append(Album("Graceland", "Paul Simon", 17))
albums2.append(Album("Whats Going On", "Marvin Gaye", 21))

# Joining album one and two
albums2.extend(albums1)

# Adding the two items in the notes
albums2.append(Album("Dark Side of the Moon", "Pink Floyd", 9))
albums2.append(Album("Oops!... I Did It Again", "Britney Spears", 16))
print(len(albums2))

# Getting the tuples of each album
str_lst_2 = [i.__str__() for i in albums2]
# Sorting them alphabetically according the the album name
# Using the first item in the tuple
# Which is the name of the album
# If a string is given it is automatically sorted alphabetically
# Number is before alphabet
str_lst_2.sort(key=lambda x: x[0])
# Printing the sorted list
print(str_lst_2)

# Finds album and returns the index
# linear search used😎
def find_album(name_album: str, album_list: list):
    # for else loop used 
    # If for loop is completed without an output
    # Meaning the item isn't in the list
    # So else will be ran 
    for index, album in enumerate(album_list):
        if name_album == album[0]: # Checking the name by index 0
            return index
    else:
        # None is used because 
        # -1 is still valid index in python
        return None # If not in list
# Print the index of the album we are searching
print(find_album("Dark Side of the Moon", str_lst_2))
