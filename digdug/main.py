from board import *

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700
running = True

# Set the screen size
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the caption
pygame.display.set_caption("DigDug")

# Paint Screen one time
pygame.display.flip()

# Load the images
player_image = pygame.image.load("images\Doug.png")
rock_image = pygame.image.load("images\Rock.png")
fygar_image = pygame.image.load("images\Fygar.png")
pookas_image = pygame.image.load("images\Pooka.png")
dirt_image = pygame.image.load("images\Dirt.png")

player = Player(100,100)
IMAGE_SCALE = (50,50)
player_image = pygame.transform.scale(player_image,IMAGE_SCALE)

class Game:
    def __init__(self):
        self.board = Board()
        self.points = 0

    def setPoints(self, points):
        self.points += points

    def getPoints(self):
        return self.points

# Main game loop
game_board = Board()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))  # Fill with black

    # Draw the game board with loaded images

    screen.blit(player_image, player.pos)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
