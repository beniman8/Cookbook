#object or recipe for an author
#definite the author class
class Author:
    def __init__(self,name,birth_year):
        self.name = name 
        self.birth_year = birth_year
    def get_author_info(self):
        return f"{self.name} (born {self.birth_year})"
    
# recipe for book 
class Book:
    def __init__(self,title,pub_year,author:Author):# book aggregate or contains another a class
        self.title = title
        self.publication_year = pub_year
        self.author = author
        
    def get_book_info(self):
        return f"'{self.title}' by {self.author.get_author_info()}, published in {self.publication_year}"
    
# Create an Author object 
author_obj = Author("George Orwell",1903)
# create a book object aggregating the Author object 
book_obj = Book("1984",1949,author_obj)

# print the book information with included author 
print(book_obj.get_book_info())