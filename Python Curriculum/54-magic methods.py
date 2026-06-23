# magic method = dunder methods (double underscore) __intit__, __str__, __eq__
#                they are automatically called by many of python's built-in operations
#                they allow developers to define or customise the behaviour of objects

class Book:

    def __init__(self, title, author, numpages):
        self.title = title 
        self.author = author 
        self.numpages = numpages 

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.numpages}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    # allows us to compare two objects using the less than and greater than operators. it is called when we use the < operator
    def __lt__(self, other): # can create a separate method for __gt__
        return self.numpages < other.numpages
    
    def __add__(self, other):
        return self.numpages + other.numpages
    
    def __contains__(self, keyword): # make contain of objects(books) iterable. allow to use the 'in' operator to check if a keyword is in the title or author of the book
        return keyword in self.title or keyword in self.author

    def __len__(self):
        return self.numpages
    
    def __getitem__(self, key): 
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        else:
            return f"{key} is invalid. Please use 'title' or 'author'."


book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
book2 = Book("if you give a mouse a cookie", "Laura Numeroff", 32)

#this is what we've been doing up to now, we can access the attributes of the class using the dot operator
print(f"Title: {book1.title}, Author: {book1.author}, Pages: {book1.numpages}")
print(f"Title: {book2.title}, Author: {book2.author}, Pages: {book2.numpages}")

""" defining the __str__ method allows to customize the string representation of the object """
print(book1) # Title: The Great Gatsby, Author: F. Scott Fitzgerald, Pages: 180
print(book2) 
# without the magic method __str__ the output is the class name and memory addr: <__main__.Book object at 0x000001F3D4B1C250>

""" comparing titles and authors of two books using the __eq__ method """
print(book1 == book2) # False. without the __eq__ method, Python compares object addresses and returns False. with the __eq__ method, it compares the title and author of the books and returns False

""" comparing the number of pages of two books using the __lt__ method """
print(book1 < book2) # False
print(book1 > book2) # True

""" adding the number of pages of two books using the __add__ method """
print(book1 + book2) # 212

""" checking if a keyword is in the title or author of the book using the __contains__ method """
print("Great" in book1) # True. this is a built-in method that checks if a substring is in a string

""" getting the number of pages of a book using the __len__ method """
print(len(book1)) # 180

""" getting the title and author of a book using the __getitem__ method """
print(book1["title"]) # The Great Gatsby
print(book2["author"]) # F. Scott Fitzgerald