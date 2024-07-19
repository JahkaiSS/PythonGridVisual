import pygame
from sys import *


pygame.init()
pygame.display.init()
pygame.font.init()

def colorMaker(r,g,b):
    return[r*255,g*255,b*255]

currentFont = pygame.font.get_fonts()[151]
secondFont = pygame.font.get_fonts()[8]
small = 12
medium = 24 
large = 40

class Font():
    def __init__(self, font_file, font_size, boldOrNot):
        self.font_file = font_file
        self.font_size = font_size
        self.boldOrNot = boldOrNot
    def makeFont(self, text, color):
        font = pygame.font.SysFont(self.font_file,self.font_size,self.boldOrNot)
        cheese = font.render(text, False, color)   
        return cheese
font = Font(currentFont,medium,True).makeFont('GRID VISUAL IN PYGAME',colorMaker(.9,.2,.1))
font_mos_pos = Font(secondFont,medium+5,False)


class Screen():
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def makeScreen(self):
        return pygame.display.set_mode((self.width,self.height))
class Line():
    def __init__(self, surface, color, start_coord, end_coord, thickness):
        self.surface = surface
        self.color = color
        self.start_coord = start_coord
        self.end_coord = end_coord
        self.thickness = thickness
    def draw(self):
        pygame.draw.line(self.surface, self.color, self.start_coord, self.end_coord, self.thickness)
class Circle():
    def __init__(self, surface, color, center_coord, radius, width):
        self.surface = surface
        self.color = color
        self.center_coord = center_coord
        self.radius = radius
        self.width = width
    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.center_coord, self.radius, self.width)

screen = Screen(500,500)
screen = screen.makeScreen()
pygame.display.set_caption('GRID VISUAL')
pygame_icon = pygame.image.load('sliderBar/filesystems_thefolder_641.ico')
pygame.display.set_icon(pygame_icon)


line = Line(screen,'BLACK',(0,10),(500,10),5)
mos_line = Line(screen,'BLACK',(10,500),(10,0),5)


gridX_line = Line(screen,'WHITE',[250,10],[250,500],1)
gridY_line = Line(screen,'WHITE',[10,250],[500,250],1)

circle_center = [250,10]
circle = Circle(screen,'YELLOW',circle_center,10,0)

circle2_center = [10,250]
circle2 = Circle(screen,'ORANGE',circle2_center,10,0)

run = True


dynamColor = [.3,1,1]

invert = 1

clock = pygame.time.Clock()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            run = False
    screen.fill(colorMaker(.5,.5,.48))
    screen.blit(font,(80,20))

    line.draw()
    mos_line.draw()
    gridX_line.draw()
    gridY_line.draw()
    circle.draw()
    circle2.draw()
    mos_pos = pygame.mouse.get_pos()
    cheese = font_mos_pos.makeFont(f'coords: {mos_pos[0], mos_pos[1]}',colorMaker(dynamColor[0],dynamColor[1],dynamColor[2]))
    if dynamColor[0] < .95 and invert == 1:
        dynamColor[0] += .005
    if dynamColor[0] > .95:
        invert = -1
    if invert == -1 and dynamColor[0] > .05:
        dynamColor[0] -= .005
    if dynamColor[0] < .05:
        invert = 1


    # print(dynamColor[0])
    screen.blit(cheese,(150,400))

 
    # print(mos_pos)
    circle_center[0] = mos_pos[0]
    circle2_center[1] = mos_pos[1]
    gridX_line.start_coord[0] = mos_pos[0]
    gridX_line.end_coord[0] = mos_pos[0]


    gridY_line.start_coord[1] = mos_pos[1]
    gridY_line.end_coord[1] = mos_pos[1]
  


    pygame.display.update()
    clock.tick(60)

    