"""
Author : Brodie Busby
A python file to hold the object classes (Object,Player,Pooka,Fygar,Rock,Dirt)
"""
import pygame 

class Object:
    """"
    A Class for a Object
    """ 
    def __init__(self, x, y):
        self.pos = (x, y)
        self.hasAnimation = False
        self.animationList = []
        self.health = 100
        self.name = "object"
    def getName(self):
        return self.name
    def setName(self,name):
        self.name = name
    
    
    def setPosition(self, x, y):
        """
        Set new x and ney y
        Input: X, Y
        """
        self.x = x
        self.y = y
    def getPosition(self):
        """
        Get position
        """
        return self.pos
    
    
    def setAnimation(self, animationList):
        """
        Set animation for objects
        Input: animationList:List
        """
        
        self.animationList = animationList

    def getAnimation(self):
        """
        Returns animationList:List
        """
        return self.animationList
    
    def move(self):
        """Default constructor for movement"""
        pass
    

    def setHealth(self, health):
        """
        Set health
        Input: health:int
        """
        self.health = health

    def getHealth(self):
        """
        Get health
        """
        return self.health


class Player(Object):
    """"
    A Class for a Player object
    
    """    
    
    def __init__(self, x, y):
        super().__init__(x, y)
        self.isUsingSpear = False
        self.name = "player"
    def useSpear(self):
        pass
    
    
def move(self):
    """Move the player"""
    
    # Each object should be 50 pixels apart
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        self.pos = self.pos[0] + 50 
    if keys[pygame.K_a]:
        self.pos = self.pos[0] - 50
    if keys[pygame.K_w]:
        self.pos = self.pos[1] - 50  
    if keys[pygame.K_s]:
        self.pos = self.pos[1] + 50

        


class Enemy(Object):
    """"
    A Class for a Enemy object
    
    """
    def __init__(self, x, y):
        super().__init__(x, y)
    def move(self):
        pass

class Dirt(Object):
    
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "dirt"

        
        
class Rock(Object):
    """"
    A Class for a Rock object
    
    """
    
    def __init__(self, x, y):
        super().__init__(x, y)
        self.playerUnder = False
        self.name = "rock"

    def fall(self):    
        """ If there is nothing under the rock fall down"""
        
        if self.y - 1 != None:
            self.y = self.y - 1


class Fygar(Enemy):
    """"
    A Class for a Fygar Enemy object
    
    """
   
    def __init__(self, x, y):
        super().__init__(x, y)
        self.isBreathingFire = False
        self.name = "fygar"

    def breathFire(self):
        pass


class Pooka(Enemy):
    """"
    A Class for a Pooka Enemy object
    
    """   

    def __init__(self, x, y):
        super().__init__(x, y)
        self.isBreathingFire = False
        self.name = "pooka"



