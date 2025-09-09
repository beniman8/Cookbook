from abc import ABC,abstractmethod
# define an abstract class called animal 
class Animal(ABC):
    
    @abstractmethod
    def sound(self):
        pass 
    
    # make a the description method abstract but provide basic implementation
    @abstractmethod
    def description(self):
        print(f"{self.__class__.__name__} says: {self.sound()}")
        
# define a concrete class 'dog' that inherits from animal 
class Dog(Animal):
    def sound(self):
        return "Woof!"
    
    # override the description method in the dog class and call the base class implementation
    def description(self):
        return super().description()
    
# define a concrete class 'cat' that inherits from animal 
class Cat(Animal):
    def sound(self):
        return "meow!"
    
    # override the description method in the cat class and call the base class implementation
    def description(self):
        return super().description()
    
    
# create instances of concrete classes and use the overridden description method
dog = Dog()
dog.description()

cat = Cat()
cat.description()

