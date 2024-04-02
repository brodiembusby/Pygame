# This is pong created using pygame by Brodie Busby 


import pygame   # import the pygame module

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Pong Remake')
clock = pygame.time.Clock()
running = True

# Ball details such as position and speed
ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
ball_speed = pygame.Vector2(6, 6)  # Adjust the ball's initial speed as needed

# Player details such as position and speed
player_1_pos = pygame.Vector2(screen.get_width() - 50, 100)
player_2_pos = pygame.Vector2(10, 200)
player_width = screen.get_width() / 40
player_height = screen.get_height() * .3

# Font for the text on the screen
font = pygame.font.Font('freesansbold.ttf', 32)

# Instatiate score variables
player_1_score = 0
player_2_score = 0

# Main game loop
while running:
    #Detect if the user wants to quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Draw the background
    screen.fill("black")
    #Set the fps
    clock.tick(60)
    
    #Draw the text on the screen
    player1_text = font.render(f'Player 1: {player_1_score}', True, "blue")
    player1_text_pos = (0,0)
    player2_text = font.render(f'Player 2: {player_2_score}', True, "red")
    player2_text_pos = (1050,0)
    screen.blit(player1_text, player1_text_pos)
    screen.blit(player2_text, player2_text_pos)
    
    # Draw the ball
    pygame.draw.circle(screen, "white", ball_pos, 10)

    # Update ball position
    ball_pos += ball_speed

    # Check ball for collision with players
    if (
        ball_pos.x - 10 <= player_2_pos.x + player_width
        and player_2_pos.y < ball_pos.y < player_2_pos.y + player_height
    ):
        ball_speed.x = abs(ball_speed.x)  # Reverse the x-direction
    elif (
        ball_pos.x + 10 >= player_1_pos.x
        and player_1_pos.y < ball_pos.y < player_1_pos.y + player_height
    ):
        ball_speed.x = -abs(ball_speed.x)  # Reverse the x-direction

    if ball_pos.x <= 0 or ball_pos.x >= screen.get_width():
        # Ball hit the left or right boundary
        # Handle scoring, reset ball position,
        if ball_pos.x <= 30:
            player_2_score += 10
        if ball_pos.x >= screen.get_width():
            player_1_score += 10
        ball_pos.x = screen.get_width() / 2

    if ball_pos.y <= 0 or ball_pos.y >= screen.get_height():
        ball_speed.y = -ball_speed.y  # Reverse the y-direction

    # Draw the players
    pygame.draw.rect(screen, "red", (player_1_pos.x, player_1_pos.y, player_width, player_height), 0)
    pygame.draw.rect(screen, "blue", (player_2_pos.x, player_2_pos.y, player_width, player_height), 0)
   
    # Update player position so it doesn't go out of the screen
    if player_1_pos.y <= 0 :
        player_1_pos.y += 50
    if player_2_pos.y <= 0 :
        player_2_pos.y += 50
    if player_1_pos.y + player_height >= screen.get_height() :
        player_1_pos.y -= 50
    if player_2_pos.y + player_height >= screen.get_height() :
        player_2_pos.y -= 50
    # Keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_1_pos.y -= 30
    if keys[pygame.K_DOWN]:
        player_1_pos.y += 30
    if keys[pygame.K_w]:
        player_2_pos.y -= 30
    if keys[pygame.K_s]:
        player_2_pos.y += 30

    pygame.display.flip()

pygame.quit()