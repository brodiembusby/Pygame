"""
Author : Brodie Busby
A python file to hold the object classes (Object,Player,Pooka,Fygar,Rock,Dirt)
"""
import pygame 
import constant
from random import randint
class Object:
    """"
    A Class for a Object
    """ 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.health = 100
        self.name = "object"
        self.orientation = "Right"
    
    def getName(self):
        return self.name
    
    def setName(self,name):
        self.name = name
    
    def getOrientation(self):
        return self.orientation
    
    def setOrientation(self,orientation):
        self.orientation = orientation
    
    def setPosition(self, x, y):
        """
        Set new x and ney y
        Input: X, Y
        """
        self.x = x
        self.y = y
        self.pos = (x, y)
        
    def getPosition(self):
        """
        Get position
        """
        return self.pos
    def setX(self,x):
        self.x = x
        self.pos = (self.x, self.y)
    def setY(self,y):
        self.y = y
        self.pos = (self.x, self.y)
      
    def getX(self):
         return self.x
     
    def getY(self):
         return self.y
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
    
    def getRect(self):
        """
        Get rect, 50, 50 is the collison around object
        """
        return pygame.Rect(self.x, self.y, 40 , 40)
    def can_move(self, new_x, new_y, game_board):
        new_rect = pygame.Rect(new_x, new_y, 50, 50)
        for obj in game_board:
            if obj is not None and obj != self:
                if new_rect.colliderect(obj.getRect()):
                    return False
        return True
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
        # key = pygame.key.get_pressed()
        # if key[pygame.K_SPACE]:
            
        
    def move(self):
        """Move the player"""
        keys = pygame.key.get_pressed()
        # Right
        if keys[pygame.K_d]:
            self.setPosition(self.getX() + .33, self.getY())
            self.orientation = "Left"
        # Left
        if keys[pygame.K_a]:
            self.setPosition(self.getX() - .33, self.getY())
            self.orientation = "Right"
        # Up
        if keys[pygame.K_w]:
            self.setPosition(self.getX(), self.getY() - .33)
        # Down
        if keys[pygame.K_s]:
            self.setPosition(self.getX(), self.getY() + .33)



class Enemy(Object):
    """"
    A Class for a Enemy object
    
    """
    def __init__(self, x, y):
        super().__init__(x, y)
    


    def move(self, game_board):
        random_direction = randint(1, 4)
        walking_pace = randint(1, 500)
        if walking_pace > 1:  # Randomly allow movement to be less frequent
            return

        if random_direction == 1:  # Move right
            new_x = self.getX() + 50
            new_y = self.getY()
            if self.can_move(new_x, new_y, game_board):
                self.setPosition(new_x, new_y)
        elif random_direction == 2:  # Move left
            new_x = self.getX() - 50
            new_y = self.getY()
            if self.can_move(new_x, new_y, game_board):
                self.setPosition(new_x, new_y)
        elif random_direction == 3:  # Move up
            new_x = self.getX()
            new_y = self.getY() - 50
            if self.can_move(new_x, new_y, game_board):
                self.setPosition(new_x, new_y)
        elif random_direction == 4:  # Move down
            new_x = self.getX()
            new_y = self.getY() + 50
            if self.can_move(new_x, new_y, game_board):
                self.setPosition(new_x, new_y)

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

    def fall(self,game_board):    
        """ If there is nothing under the rock fall down"""
        
        new_x = self.getX()
        new_y = self.getY() + 50
        if self.can_move(new_x, new_y, game_board):
            self.setPosition(new_x, new_y)
            


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
        self.name = "pooka"
