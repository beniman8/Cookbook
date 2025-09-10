from abc import ABC , abstractmethod


# define abstract class shape 

class Shape(ABC):
    
    def __init__(self,color):
        self.color = color 
        
    @abstractmethod
    def area(self):
        pass 
    
    @abstractmethod
    def perimeter(self):
        pass
    
    # make the description a base implementation 
    def description(self):
        print(f"{self.__class__.__name__} has the color: {self.color}")
        
        
# define the concrete class rectangle 

class Rectangle(Shape):
    def __init__(self,width,height, color):
        super().__init__(color)
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 *(self.width + self.height)
    
    
class Circle(Shape):
    def __init__(self,radius, color):
        super().__init__(color)
        
        self.radius = radius
        
    def area(self):
        from math import pi,pow
        
        return pi * pow(self.radius,2)
    
    def perimeter(self):
        return 2 * 3.141592653589793 * self.radius
    
    
#interface contract method 
def process_my_color(obj:Shape):
    obj.description()
    

# create instance of concrete classes and use their methods 
rectangle = Rectangle(4,5,'blue')
print(f"Rectangle area: {rectangle.area()}")
print(f"Rectangle perimeter: {rectangle.perimeter()}")
print(f"Rectangle color: {rectangle.color}")

circle = Circle(3,'red')
print(f"Circle area: {circle.area():.2f}")
print(f"Circle perimeter: {circle.perimeter():.2f}")
print(f"Circle color: {circle.color}")


process_my_color(rectangle)
process_my_color(circle)
