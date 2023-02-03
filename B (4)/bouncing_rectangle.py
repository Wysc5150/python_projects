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
pygame.init()
pygame.mixer.init()
WIDTH = 700
HEIGHT = 500
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game Window")

clock = pygame.time.Clock()
FPS = 60
basic_font = pygame.font.SysFont('Arial', 48)

rect_x=50
rect_y=50
rect_change_x=5
rect_change_y=3

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

    pygame.draw.rect(screen, color2, [rect_x,rect_y,50,50])
    rect_x+=rect_change_x
    rect_y+=rect_change_y

    if rect_x>649 or rect_x<0:
        rect_change_x*=-1
    if rect_y>449 or rect_y<0:
        rect_change_y*=-1

    pygame.display.update()


pygame.quit()
sys.exit()