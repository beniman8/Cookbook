# this is a program that calculates the are of a rectangle  Area = width x length



class Rectangle:
    
    def __init__(self,width,length):
        self.width=width
        self.length = length
        
        
    def area(self):
        
        area = self.width * self.length
        
        print(area)
    
    
rectangle = Rectangle(5,5)
rectangle.area()
    
