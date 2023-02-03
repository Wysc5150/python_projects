# Cameron Wysocki
# 1/24/23
# Multi Bouncing 

# import
import pygame as py
import random as pain
import sys
import os 

ORANGE = (235,97,35)
REDPINK = (205, 0, 123)

# intialize
py.init()
py.mixer.init()
# display
WIDTH = 800
HEIGHT = 600
size = (WIDTH, HEIGHT)
screen = py.display.set_mode(size)
py.display.set_caption("Bouncing Block 2.0")
BALL_SIZE = 25
# Entities
clock = py.time.Clock()
FPS = 60

font = py.font.SysFont('Arial', 48)

class Ball():
    def __init__(self,ballRect, speed,color = None):
        self.ballRect = ballRect
        self.speed = speed
        self.color = color if color != None else [pain.randint(0, 255)for _ in range(3)]

    def update(self,screen):
        if not 0 < self.ballRect.x < screen.get_width() - self.ballRect.width - 1:
            self.speed.x *= -1

        if not 0 < self.ballRect.y < screen.get_height() - self.ballRect.height - 1:
            self.speed.y *= -1

        self.ballRect.topleft += self.speed
        py.draw.ellipse(screen,self.color,self.ballRect)

ball = []


# Loop
keep_looping = True
while keep_looping:

    clock.tick(FPS)


    for event in py.event.get():
        if event.type == py.QUIT:
            keep_looping = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_q:
                keep_looping = False

            

            if event.key == py.K_SPACE:
                ball.append(Ball(py.Rect(pain.randint(0,749), pain.randint(0,549), 50, 50), py.Vector2(20,20)))

        if event.type == py.MOUSEWHEEL:
                ball.append(Ball(py.Rect(pain.randint(0,749), pain.randint(0,549), 60, 60), py.Vector2(20,20)))




    screen.fill(REDPINK)

    # py.draw.rect(screen, ORANGE,[50,50])

    for Balls in ball:
        Balls.update(screen)
    
    py.display.update()
py.quit()
