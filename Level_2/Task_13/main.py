# Only run this file.
# File for executing the code
from database.data_base import *
from UI.UI import user_interface


def main():
    user_interface()
    db.commit()

if __name__ == '__main__':
    main()
    