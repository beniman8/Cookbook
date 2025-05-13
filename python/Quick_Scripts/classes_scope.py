'''
since every method has a reference to the class it is easy 
to change the class attribute 

that is the reason why methods rely much less on parameters , global and return 

object can be change from outside or from a local scope of a function 

'''

#scope problem 

# def update_health(amount):
#     global health
#     health += amount
    
# health = 10 

# print(health)
# update_health(20)
# print(health)

def update_health(amount):
    
    monster.health += amount

class Monster:
    
    def __init__(self,health,energy) -> None:
        self.health = health
        # self.set_energy(energy)
        self.energy = energy
    def update_energy(self,amount):
        self.energy += amount
        
    # def set_energy(self,energy):
    #     new_energy = energy * 2
    #     self.energy = new_energy
    
    def get_damage(self,amount):
        self.health -= amount
        
    
    
monster = Monster(health=100,energy=80)
# print(monster.health)
# update_health(20)
# print(monster.health)

#monster.update_energy(45)
#print(monster.energy)

# exercise 
# 1 create a hero class with 2 parameters: damage, monster
# 2 the monster class should have method that lowers the health -> get_damage(amount)
# 3 the hero class should have an attack method that calls the get_damage method from the monster 
# the amount of damage is hero.damage

class Hero:
    
    def __init__(self,damage,monster) -> None:
        self.damage = damage 
        self.monster = monster  
        
    def attack(self):
        
        self.monster.get_damage(self.damage)
   
hero = Hero(10,monster)
hero.attack()
print(monster.health)