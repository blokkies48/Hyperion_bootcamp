# Import that is needed
import xml.etree.ElementTree as tree 

# Setting the root 
root = tree.parse("movie.xml").getroot() 
# Function for getting the child of movie tag
def get_child_of_movie(root): # Root passed to function
    get_element = False # Test if element should be printed
    fav_count = 0 # Setting fav count to 0
    not_fav_count = 0 # Setting not_fav count to 0
    for child in root.iter(): # Iterating over all the elements
        # If element is movie then get element is set to True
        if child.tag == "movie":
            get_element = True
            # Help differentiate between movies
            print()
        # decade the element directly after movie
        # Sets get element to false
        # To not print not wanted tags
        elif child.tag == "decade" or child.tag == "genre":
            get_element = False

        # If get element is True
        # Then tag is printed
        if get_element:
            print(child.tag)
            # If tag is description 
            # The text of the element is printed
            if child.tag == "description":
                print("".join(child.itertext()))
            # Getting favourite count by
            # Checking for true in the attributes dict of movie
            # child.tag == "movie" to avoid crashes
            # If conditions are met fav_count is increased by 1
            if child.tag == "movie" and child.attrib["favorite"] == "True":
                fav_count += 1
            # Same logic as above
            # Just for not the favorite count
            elif child.tag == "movie" and child.attrib["favorite"] == "False":
                not_fav_count += 1
    # Printing the number of favourites and none favourites
    # After for loop iteration
    print(f"\nThe number of favourites are {fav_count}\nThe number of not favourites are {not_fav_count}")
                


# Main function to run code
def main():
    get_child_of_movie(root)              

# Indicate this file should be ran
if __name__ == '__main__':
    main()
    