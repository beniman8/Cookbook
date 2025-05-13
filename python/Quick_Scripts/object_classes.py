"""
objects is a container for variable and functions

for example a monster object in a game might have variable such as health energy stamina damage

and functions for attack movement animation

the variables and functions of an object only exist inside the object


variables in an object are called attributes 
functions in an object are called methods


you can create multiple objects, in those objects the attributes can change 
but the methods remain the same.

but each objects gets their ow attributes and methods


what is a class  

a class is a blueprint for an object
when creating an object we first need a class

a class accepts arguments to customize the object we would like to create

a class can also inherit from another class 
meaning the resulting object will have attributes and methods from both classes

classes and object help organize complex code that can be reusable all over your program

classes are use everywhere 

when you call a method aka a function inside of a class 
python passes a reference to the objected created by the class as the first argument in the method

so if you create a monster class it is going to pass itself to all methods created in that class
"""


class Monster:

    # attributes
    health = 90
    energy = 40

    # methods
    def attack(self, amount):
        print("The monster attacked")
        print(f"{amount} damage was dealt")
        self.energy -= amount
        print(self.energy)

    def move(self, speed):
        print(f"the monster has moved at {speed} speed")


monster = Monster()
print(monster.health)
print(monster.energy)
monster.attack(10)
monster.move(12)
