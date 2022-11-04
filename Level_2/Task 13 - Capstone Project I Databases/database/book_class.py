# Creating book objects
class Book:
    def __init__(self, Id, Title, Author, Qty):
        self.Id = Id
        self.Title = Title
        self.Author = Author
        self.Qty = Qty

    # Tuple needed to add to database
    def add_to_db(self):
        return (self.Id, self.Title, self.Author, self.Qty)
