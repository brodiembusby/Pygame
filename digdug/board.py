"""
Author : Brodie Busby
A python file to hold the board class
"""
from object import *
import constant

# Dictionary to convert text to objects
char_to_class = {"p": Player,  "r": Rock, "f": Fygar, "o": Pooka, "d": Dirt, None: None}

class Game:
    """
    A class representing a board automatically sets up a board with
    a list of characters as input 
    """
    def __init__(self):
        self.board = []
        self.points = 0

    def setPoints(self, points):
        self.points += points

    def getPoints(self):
        return self.points
    
    def getBoard(self):
        return self.board
        
    def generateBoard(self, text_board):
        """
        Convert a text board to a board with objects instead of text.
        Input: text_board
        Output: object filled list
        """
        new_board = []
        temp_x = 0  
        temp_y = 50
        for char in text_board:      
            if char in char_to_class:
                if char == None:  # If None Append and move on
                    new_board.append(None)
                    temp_x += 50
                    continue
                obj = char_to_class[char](temp_x, temp_y)  # Turns character into object
                new_board.append(obj)  # Adds object into list
                temp_x += 50
                if temp_x >= constant.SCREEN_WIDTH:  # Once width is reached start next row
                    temp_x = 0
                    temp_y += 50           
            if temp_y >= constant.SCREEN_HEIGHT:  # if bigger than screen height stop
                # Set the board
                self.board = new_board
        # Set the board       
        self.board = new_board