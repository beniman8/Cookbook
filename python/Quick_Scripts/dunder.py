'''
the Dunder methods 

__Dunder__  methods

double underscore methods

dunder method is a method that is not called by the user.
it is called by python when something happens

__init__ is called when the object is created 
__len__ is called when the object is passe into len()

'''


from typing import Any


class Monster:

    # attributes
    # health = 90
    # energy = 40
    
    def __init__(self,health,energy) -> None:
        self.health = health
        self.energy = energy
        print('The monster was created')
        
    def __len__(self):
        return self.health
    
    def __abs__(self):
        return self.energy
    
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print('The monster was called')

    def __add__(self,other):
        
        print(self.health+other)
        
    def __str__(self) -> str:
        return f'This monster has {self.health} health and {self.energy} energy'
    # methods
    def attack(self, amount):
        print("The monster attacked")
        print(f"{amount} damage was dealt")
        self.energy -= amount
        print(self.energy)

    def move(self, speed):
        print(f"the monster has moved at {speed} speed")
        
monster1 = Monster(health=100,energy=50)
monster2 = Monster(80,77)

print(monster1.health)
print(len(monster1))
monster1()
monster1+4

print(monster1)
print(str(monster1))
print(monster1.__str__())
