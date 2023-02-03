import pygame
import os



# initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load(os.path.join('ufo.png'))
pygame.display.set_icon(icon)

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

# RGB
screen.fill((255,0,0))
pygame.display.update()