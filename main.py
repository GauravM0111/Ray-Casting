from random import randint
import pygame
from boundary import Boundary
from configurations import Configuration
from ray import Ray
from raySource import RaySource

config = Configuration()
numBoundaries = 5
raySourceAngleOffset = 1
timeDelay = 0
boundaries = []

# initializes game
pygame.init()

# Set up the drawing window (surface object)
screen = pygame.display.set_mode(config.displaySize)

for i in range(numBoundaries):
    x1 = randint(0, config.displaySize[0])
    y1 = randint(0, config.displaySize[1])
    x2 = randint(0, config.displaySize[0])
    y2 = randint(0, config.displaySize[1])
    boundary = Boundary(x1, y1, x2, y2)
    boundaries.append(boundary)

lbond = Boundary(5, 5, 5, config.displaySize[1]-5)
rbond = Boundary(config.displaySize[0]-5, 5, config.displaySize[0]-5, config.displaySize[1]-5)
bbond = Boundary(5, config.displaySize[1]-5, config.displaySize[0]-5, config.displaySize[1]-5)
tbond = Boundary(5, 5, config.displaySize[0]-5, 5)
boundaries.append(lbond)
boundaries.append(rbond)
boundaries.append(bbond)
boundaries.append(tbond)

for boundary in boundaries:
    boundary.draw(screen)

raySource = RaySource(raySourceAngleOffset)

# Flip the display
pygame.display.flip()

# Game loop
running = True
while running:
    pygame.time.delay(timeDelay)
    
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x, y = pygame.mouse.get_pos()
    
    screen.fill(config.black)

    # draw the boundaries
    for boundary in boundaries:
        boundary.draw(screen)

    # update ray source position and draw
    raySource.updateOrigin(x, y)
    raySource.draw(screen, boundaries)

    pygame.display.update()

# Done! Time to quit.
pygame.quit()