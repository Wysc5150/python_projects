import pygame as py
import random as pain
import sys
import os 

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# intialize
py.init()
py.mixer.init()
# display
WIDTH = 800
HEIGHT = 600
size = (WIDTH, HEIGHT)
screen = py.display.set_mode(size)
py.display.set_caption("Alien again")
# Entities
clock = py.time.Clock()
FPS = 60

font = py.font.SysFont('Arial', 48)


rect_x=399
rect_y=249
rect_x2=351
rect_y2=201
rect_x3=399
rect_y3=249
rect_change_x=5
rect_change_y=3
rect_change_x2=5
rect_change_y2=3

# Loop
keep_looping = True
while keep_looping:

    clock.tick(FPS)


    for event in py.event.get():
        if event.type == py.QUIT:
            keep_looping = False

    screen.fill(WHITE)
    draw = py.draw.rect(screen, BLACK, (rect_x2, rect_y2, 48, 48))
    draw = py.draw.rect(screen, BLACK, (rect_x2, rect_y, 48, 48))
    draw = py.draw.rect(screen, BLACK, (rect_x, rect_y2, 48, 48))
    draw = py.draw.rect(screen, BLACK, (rect_x, rect_y, 48, 48))
    draw = py.draw.circle(screen,BLACK,(rect_x, rect_y),55)
    draw = py.draw.circle(screen,WHITE,(rect_x, rect_y),30)
    draw = py.draw.circle(screen,RED,(rect_x, rect_y),20)
    draw = py.draw.circle(screen,BLACK,(rect_x, rect_y),10)
    
    
    rect_x+=rect_change_x
    rect_y+=rect_change_y

    if rect_x>749 or rect_x<49:
        rect_change_x*=-1
    if rect_y>549 or rect_y<49:
        rect_change_y*=-1

    rect_x2+=rect_change_x2
    rect_y2+=rect_change_y2

    if rect_x>749 or rect_x<49:
        rect_change_x2*=-1
    if rect_y>549 or rect_y<49:
        rect_change_y2*=-1



    py.display.update()
py.quit()