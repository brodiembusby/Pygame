import pygame
from object import *
from board import *

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Game:
    def __init__(self):
        self.board = Board()
        self.points = 0

    def scoreBoard(self):
        return self.points

    def run(self):
        pass

    def setPoints(self, points):
        self.points += points

    def getPoints(self):
        return self.points

# Main game loop
game = Game()
while True:
    game.run()
