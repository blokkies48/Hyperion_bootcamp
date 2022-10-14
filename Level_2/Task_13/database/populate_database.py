from database.book_class import Book

# This is what is initially added when database is created.
book_1 = Book(3001, "A Tale of Two Cities", "Charles Dickens", 30)
book_2 = Book(3002, "Harry Potter and the Philosopher's Stone", "J.K Rowling", 40)
book_3 = Book(3003, "The Lion, the Witch and the Wardrobe", "C.S Lewis", 25)
book_4 = Book(3004, "The Lord of the Rings", "J.R.R Tolkien", 37)
book_5 = Book(3005, "Alice in Wonderland", "Lewis Carroll", 12)

# List of book objects
books = [
    book_1.add_to_db(),
    book_2.add_to_db(),
    book_3.add_to_db(),
    book_4.add_to_db(),
    book_5.add_to_db()
    ]