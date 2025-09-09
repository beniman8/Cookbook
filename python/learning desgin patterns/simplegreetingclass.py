
############################# GREETING RECIPE/OBJECT  ###########

# Define the greeting class
class Greeting:
    # Constructor for the greeting class 
    def __init__(self, name):
        self.name = name 
        
    # Define our greeting method 
    def say_hello(self):
        #print a personalized greeting message 
        # using the 'name' attribute 
        print(f"Hello, {self.name} !")
        
############################# GREETING RECIPE/OBJECT  ###########

# Create an object of the greeting class,
# initializing it with the name 'Jhon'
greeting = Greeting("jhon")

# Call the 'say_hello' method on the 'greeting'
# object to print the greeting message 
greeting.say_hello()


#object or recipe for an author

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


################################ inheritance   ##########################################

# Base (parent) class 
class Animal:
    def __init__(self,name):
        self.name = name 

    def speak(self):
        print(f"{self.name} makes a sound.")


# Derived (child) class 
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")


# Derived (child) class 
class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows.")

cat = Cat('lola')
cat.speak()