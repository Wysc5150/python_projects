WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

color=BLUE
color2=RED
color3=GREEN

def rgb(color):
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

def rgb2(color, color2):
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

def rgb3(color, color2, color3):
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