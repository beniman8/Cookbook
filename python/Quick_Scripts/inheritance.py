"""
inheritance just mean one class get the attributes and method of another class or classes 



"""


class Monster:
    # health = 50 
    # energy = 100

    def __init__(self, health, energy) -> None:
        self.health = health
        self.energy = energy

    # methods
    def attack(self, amount):
        print("the monster has attacked!")
        print(f"{amount} damage was dealt")
        self.energy -= 20

    def move(self, speed):
        print("The monster has moved")
        print(f"It has a speed of {speed}")
        
class Shark(Monster):
    
    def __init__(self,speed,health, energy) -> None:
        super().__init__(health, energy)
        self.speed = speed
        
    def bite(self):
        print('The shark has bitten you !')

    #overwriting move from the parent class 
    def move(self):
        
        print('The shark has moved')
        print(f'the speed of the shark is {self.speed}')

shark = Shark(speed=452,health=100,energy=80)
print(shark.energy)
print(shark.speed)
shark.move()

# exercise 

# create scorpion class that inherits from monster
# health and energy from the parent
# poison_damage attribute 
# overwrite the damage method to show poison damage 

class Scorpion(Monster):
    
    def __init__(self, health, energy,poison_damage) -> None:
        super().__init__(health, energy)
        
        self.poison_damage = poison_damage
    
    def attack(self):
        print('The scorpion has sprayed his poison')
        print(f"{self.poison_damage} poison damage was dealt")
        self.energy -= self.poison_damage
        
scorpion = Scorpion(health=100,energy=67,poison_damage=5)

scorpion.attack()
print(scorpion.energy)