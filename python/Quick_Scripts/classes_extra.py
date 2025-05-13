

class Monster:
    '''
    A monster that has some attributes
    '''

    def __init__(self, health, energy,**kwargs) -> None:
        self.health = health
        self.energy = energy
        # private attributes
        self._id = 5
        
        super().__init__(**kwargs)

    def attack(self, amount):
        
        print("The monster has attacked!!")
        print(f"{amount} damage was dealt")
        self.energy -= 20

    def move(self, speed):
        print("The monster has moved!")
        print(f"It has a speed of {speed}")
        
        
monster = Monster(100,85)



# hasattr and setattr
print(hasattr(monster,'health'))

if hasattr(monster,'health'):
    print(f'The monster has {monster.health} health')
    
setattr(monster,'weapon','gun')
#monster.weapon = 'sword' these are the same thing 
print(monster.weapon)


new_attributes = (['weapon','Axe'],['Armor','Shield'],['Potion','Mana'])

for attribute,value in new_attributes:
    setattr(monster,attribute,value)
    
print(vars(monster))
# docstring 

print(monster.__doc__)
help(monster)