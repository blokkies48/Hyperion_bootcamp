class Album(): 
    def __init__(self, album_name: str, artist_name: str, number_of_songs: int):
        self.album_name = album_name
        self.artist_name = artist_name
        self.number_of_songs = number_of_songs

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
str_lst = [item.__str__() for item in albums1]
print("\nThe first albums list unsorted:\n",str_lst)
# Sorting using a lambda method to get the 3rd item
str_lst.sort(key=lambda x: x[2])
print("\nThe first albums list sorted:\n",str_lst)


def swap_positions(albums1):
    albums1[1], albums1[0] = albums1[0], albums1[1]
    return albums1

print("\nElements swapped\n",swap_positions(str_lst))

# Creating the second album list
albums2 = []

albums2.append(Album("Aquemini", "OutKast", 16))
albums2.append(Album("Legend", "Bob Marley and the Wailers", 16))
albums2.append(Album("Ramones", "Ramones", 20))
albums2.append(Album("Graceland", "Paul Simon", 17))
albums2.append(Album("Whats Going On", "Marvin Gaye", 21))

print("\nThe second album list:\n",[item.__str__() for item in albums2])

# Joining album one and two
albums2.extend(albums1)

# Adding the two items in the notes
albums2.append(Album("Dark Side of the Moon", "Pink Floyd", 9))
albums2.append(Album("Oops!... I Did It Again", "Britney Spears", 16))

# Getting the tuples of each album
str_lst_2 = [item.__str__() for item in albums2]
# Sorting them alphabetically according the the album name
str_lst_2.sort(key=lambda x: x[0])
# Printing the sorted list

print("\nSorted list of albums:\n",str_lst_2)

# Finds album and returns the index
# linear search used😎
def find_album(name_album: str, album_list: list):
    for index, album in enumerate(album_list):
        if name_album == album[0]: # Checking the name by index 0
            return index
    else:
        # None is used because 
        # -1 is still valid index in python
        return None

# Print the index of the album we are searching
print("\nThe Album searched index's:\n",find_album("Dark Side of the Moon", str_lst_2))
