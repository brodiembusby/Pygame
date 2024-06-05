"""
Author : Brodie Busby
Main game file
"""
import pygame
from board import *
import constant

# Initialize pygame
pygame.init()
# Display options
screen = pygame.display.set_mode((constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
pygame.display.set_caption("DigDug")


# Text options
pygame.font.init()              
my_font = pygame.font.SysFont('Arial', 30)

# Load the images
images = {
    "player": pygame.image.load("images/Doug.png"),
    "rock": pygame.image.load("images/Rock.png"),
    "fygar": pygame.image.load("images/Fygar.png"),
    "pooka": pygame.image.load("images/Pooka.png"),
    "dirt": pygame.image.load("images/Dirt.png")
}

player = Player(0, 50)
player_image = pygame.transform.scale(images["player"], constant.IMAGE_SCALE)
fygar_image = pygame.transform.scale(images["fygar"], constant.IMAGE_SCALE)
# Main game loop
game = Game()
game.generateBoard(constant.GAME_BOARD)
running = True



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Background colors
    screen.fill((98, 37, 37))
    screen.fill((0, 191, 255), (0, 0, constant.SCREEN_WIDTH, 100))

    # Move the player
    player.move()

    # Main Game loop
    for obj in game.getBoard():
        if obj is None:
            continue
        obj_position = obj.getPosition()
        obj_name = obj.getName()
        
        # Draw the object based on its type
        if obj_name == "rock":
            screen.blit(images["rock"], obj_position)
        elif obj_name == "fygar":
            obj.move(game.getBoard()) 
            screen.blit(fygar_image, obj_position)
        elif obj_name == "pooka":
            obj.move(game.getBoard()) 
            screen.blit(images["pooka"], obj_position)
        elif obj_name == "dirt":
            screen.blit(images["dirt"], obj_position)
        
        if player.getOrientation() == "Right":
            flipped_player_image = pygame.transform.flip(player_image, True, False)
        else:
            flipped_player_image  = player_image
            
        # Check for collision with the player
        if player.getRect().colliderect(obj.getRect()):
            if obj_name == "dirt":
                game.getBoard().remove(obj)
                game.setPoints(10)

        # Debugging rect for collisions on all objects
        # pygame.draw.rect(screen, (255, 0, 0), obj.getRect(), 2)  # Red color for other objects
    # pygame.draw.rect(screen, (0, 255, 0), player.getRect(), 2)
    
    # Display Items on screen
    screen.blit(flipped_player_image , player.getPosition())
    text_surface = my_font.render(f'Points:{game.getPoints()}', False, (0, 10, 0))
        
    screen.blit(text_surface, (425,0))
    pygame.display.flip()

# Quit Pygame
pygame.quit()