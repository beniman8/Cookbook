from abc import ABC,abstractmethod
from enum import Enum,auto

class ShipType(Enum):
    MillenniumFalcon =auto()
    UNSCInfinity =auto()
    USSEnterprise =auto()
    Serenity =auto()

#base abstract class for the spaceship
class SpaceShip(ABC):
    def __init__(self,pos,size,displayName,speed):
        self.pos = pos 
        self.size = size 
        self.displayName = displayName
        self.speed = speed
        
    @abstractmethod
    def draw(self,surface):
        pass 

# MillenniumFalcon class inheriting from SpaceShip
class MillenniumFalcon(SpaceShip):
    def __init__(self, pos, size, displayName, speed):
        super().__init__(pos, size, displayName, speed)
        
    def draw(self, surface):
        return super().draw(surface)
    
    
# spaceship factory class for creating shape instance 
class SpaceshipFactory:
    @staticmethod
    def create_spaceship(context):
        if context.ship_type == ShipType.MillenniumFalcon:
            return MillenniumFalcon((context.x,context.y),50,"MillenniumFalcon",50)
        else:
            raise ValueError("Invalid ship type")
        
class ShipContext:
    def __init__(self,ship_type,pos,size,displayName,speed):
        self.ship_type = ship_type
        self.pos = pos 
        self.size = size 
        self.displayName = displayName
        self.speed = speed
        
            