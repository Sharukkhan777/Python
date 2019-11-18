import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
DISPLAYSURF.fill((255,255,255))
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)
RED = (255, 0, 0)

pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0), (291, 106), (236, 200),(56, 277), (0, 106)))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 1)
pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 0)
pygame.draw.circle(DISPLAYSURF, GREEN, (300, 50), 10, 0)
pygame.draw.circle(DISPLAYSURF, RED, (300, 50), 5, 0)
while True: # main game loop
     for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
     pygame.display.update()
