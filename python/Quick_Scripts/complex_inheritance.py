"""
How to create a child class that inherits from 2 parents classes or more


"""


class Monster:

    def __init__(self, health, energy,**kwargs) -> None:
        self.health = health
        self.energy = energy
        super().__init__(**kwargs)

    def attack(self, amount):
        print("The monster has attacked!!")
        print(f"{amount} damage was dealt")
        self.energy -= 20

    def move(self, speed):
        print("The monster has moved!")
        print(f"It has a speed of {speed}")


class Fish:

    def __init__(self, speed, has_scales,**kwargs) -> None:
        self.speed = speed
        self.has_scales = has_scales
        super().__init__(**kwargs)

    def swim(self):
        print(f"The fish is swimming at a speed of {self.speed}")


class Shark(Monster, Fish):

    def __init__(self, health, energy, bite_strength,speed, has_scales) -> None:
        self.bite_strength = bite_strength
        super().__init__(health=health, energy=energy,speed=speed,has_scales= has_scales)


# mro -> method resolution order
# print(Shark.mro())

shark = Shark(health=100, energy=80, bite_strength=15, speed=120, has_scales=False)
print(shark.speed)
