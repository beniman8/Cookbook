# this is a program that calculates the are of a rectangle  Area = width x length



class Rectangle:
    
    def __init__(self,width,length):
        self.width=width
        self.length = length
        
        
    def area(self):
        
        area = self.width * self.length
        
        print(f"the area is {area} cm^2")
    
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
rectangle = Rectangle(width,length)
rectangle.area()
    
