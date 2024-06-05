"""
Author : Brodie Busby
A python file to run the game
"""

from board import *
import constant
# Initialize pygame
pygame.init()

# Constants
running = True

# Set the screen size
screen = pygame.display.set_mode((constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))

# Set the caption
pygame.display.set_caption("DigDug")

# Paint Screen one time
pygame.display.flip()

# Load the images
images = {
    "player": pygame.image.load("images\Doug.png"),
    "rock": pygame.image.load("images\Rock.png"),
    "fygar": pygame.image.load("images\Fygar.png"),
    "pooka": pygame.image.load("images\Pooka.png"),
    "dirt": pygame.image.load("images\Dirt.png")
}

player = Player(100,100)
IMAGE_SCALE = (100,100)
player_image = pygame.transform.scale(images["player"],IMAGE_SCALE)

class Game:
    def __init__(self):
        self.board = Board()
        self.points = 0

    def setPoints(self, points):
        self.points += points

    def getPoints(self):
        return self.points

# Main game loop
board = Board().generateBoard(constant.GAME_BOARD)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((98,37,37))  # Sky Color
    screen.fill((0,191,255),(0,0,constant.SCREEN_WIDTH,100))  # Sky Color

    # Draw the game board with loaded images
    for obj in board:
        if obj == None: # If None Append and move on
            continue
        obj_position = obj.getPosition()
        obj_type = obj.getName()
        
        # Draw the object based on its type
        if obj_type == "rock":
            screen.blit(images["rock"], obj_position)
        elif obj_type == "fygar":
            screen.blit(pygame.transform.scale(images["fygar"],(50,50)), obj_position)
        elif obj_type == "pooka":
            screen.blit(images["pooka"], obj_position)
        elif obj_type == "dirt":
            screen.blit(images["dirt"], obj_position)
        elif obj_type == "player":
            screen.blit(images["player"], obj_position)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
