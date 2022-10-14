# Only run this file.
# File for executing the code

# Importing everything needed from other files in this programme 
# No libraries used 
from database.data_base import *
from UI.UI import user_interface

# The main function contains all the code that has to be executed
def main():
    user_interface()
    
# Used to indicate that this file is what has to be executed
if __name__ == '__main__':
    main()
    