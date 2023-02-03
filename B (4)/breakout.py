# Breakout Game Starter File


import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Epileptic Breakout")

# Set up sprites and other game variables
font = pygame.font.SysFont(None, 72)
# Color constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

color=BLUE
color2=RED
color3=GREEN
color4=WHITE
color5=BLACK

bricks = []
for row in range(3):
    for col in range(10):
        brick = pygame.Rect(col * 80 + 10, row * 40 + 60, 60, 20)
        bricks.append(brick)
paddle_rect = pygame.Rect(300,500,50,20)

ball_rect = pygame.Rect(150,150,20,20)
ball_velocity= [5,5]


clock = pygame.time.Clock()
# Set number of frames per second (FPS)
FPS = 60

# WHILE loop is our game loop...
gameover = False
while not gameover:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                gameover = True
        if event.type == pygame.QUIT:
            gameover = True
   


                
    # Keep track of which keys the user has pressed and tell Pygame
    # what to do when user presses specific keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        paddle_rect[0] += 10
    elif keys[pygame.K_LEFT]:
        paddle_rect[0]-= 10
            
             
    # Move the rectangle that contains the ball
    ball_rect[0] += ball_velocity[0]
    ball_rect[1] += ball_velocity[1]

    if ball_rect[1] > 579:
        gameover = True
    elif ball_rect[1] < 0:
        ball_velocity[1] = 5
    elif ball_rect[0] > 779:
        ball_velocity[0] = -5
    elif ball_rect[0] < 0:
        ball_velocity[0] = 5

    
    


                
    # Handle collisions
    if paddle_rect.colliderect(ball_rect):
        ball_velocity[1] *= -1
    
    for brick in bricks.copy():
        if ball_rect.colliderect(brick):
            bricks.remove(brick)
            ball_velocity[1] *= -1
    # Fill screen with designated background color

    if color3==BLUE:
        color3=RED
    elif color3==RED:
        color3=GREEN
    elif color3==GREEN:
        color3=WHITE
    elif color3==WHITE:
        color3=BLACK
    elif color3==BLACK:
        color3=BLUE

    paddle_color = color3

    if color2==BLUE:
        color2=RED
    elif color2==RED:
        color2=GREEN
    elif color2==GREEN:
        color2=WHITE
    elif color2==WHITE:
        color2=BLACK
    elif color2==BLACK:
        color2=BLUE

    ball_color = color2

    if color==BLUE:
        color=RED
    elif color==RED:
        color=GREEN
    elif color==GREEN:
        color=WHITE
    elif color==WHITE:
        color=BLACK
    elif color==BLACK:
        color=BLUE

    screen.fill(color)

    if color4==BLUE:
        color4=RED
    elif color4==RED:
        color4=GREEN
    elif color4==GREEN:
        color4=WHITE
    elif color4==WHITE:
        color4=BLACK
    elif color4==BLACK:
        color4=BLUE

    brick_color = color4

    if color5==BLUE:
        color5=RED
    elif color5==RED:
        color5=GREEN
    elif color5==GREEN:
        color5=WHITE
    elif color5==WHITE:
        color5=BLACK
    elif color5==BLACK:
        color5=BLUE
    
    # Draw stuff on the screen
    pygame.draw.ellipse(screen, ball_color, ball_rect)
    pygame.draw.rect(screen, paddle_color, paddle_rect)
    for brick in bricks:
        pygame.draw.rect(screen, brick_color, brick)
    
    score_text = font.render(str(len(bricks)), True, (color5))
    screen.blit(score_text, (700,10))
    if len(bricks)==0:
        gameover=True



    # Update screen 60 times per second (FPS)
    pygame.display.update()

pygame.quit()
sys.exit()