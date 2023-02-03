# IMPORT

import pygame
import random
import sys
import os

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
color=BLUE
color2=RED
color3=GREEN

# INITIALIZE

pygame.init()

# DISPLAY

WIDTH=800
HEIGHT=600
size=(WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Epileptic Bouncing Square 2")

# ENTITIES

clock = pygame.time.Clock()
FPS = 60
basic_font = pygame.font.SysFont('Arial', 48)
font = pygame.font.Font('freesansbold.ttf', 32)



rect_x = 50
rect_y = 50
rect_change_x = 5
rect_change_y = 3

# LOOP
keep_looping = True
while keep_looping:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_looping = False

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

    text=font.render('Epilepsy', True, color3)
    textRect = text.get_rect()
    textRect.center = (WIDTH // 2, HEIGHT // 2)

    screen.blit(text, textRect)

    pygame.draw.rect(screen, color2, [rect_x,rect_y,50,50])
    rect_x+=rect_change_x
    rect_y+=rect_change_y

    if rect_x>749 or rect_x<0:
        rect_change_x*=-1
    if rect_y>549 or rect_y<0:
        rect_change_y*=-1

    pygame.display.update()


pygame.quit()
sys.exit()