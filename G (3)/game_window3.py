import pygame
import random
import sys
import os

WIDTH=700
HEIGHT=500
FPS=60

WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

pygame.init()
pygame.mixer.init()

size=(WIDTH,HEIGHT)
screen=pygame.display.set_mode(size)

pygame.display.set_caption("My Game Window")

icon=pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

clock=pygame.time.Clock()

basic_font=pygame.font.SysFont('Arial',48)

msg1='Game Over!'
my_sample_surf=basic_font.render(msg1,1,WHITE)

msg2='Programmer: Cam W'
your_sample_surf=basic_font.render(msg2,1,GREEN)

ctc_session='PM Web & App Dev'

session=(f"Session: {ctc_session.upper()}", screen.get_width()/2, screen.get_height()/2, RED,GREEN,'Arial', 42, False,True,True)
