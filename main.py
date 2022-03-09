from random import randint
import pygame
from boundary import Boundary
from configurations import Configuration
from raySource import RaySource

config = Configuration()
numBoundaries = 5
boundaries = []

# initializes game
pygame.init()
# Set up the drawing window (surface object)
screen = pygame.display.set_mode(config.displaySize)

for i in range(numBoundaries):
    x1 = randint(-config.center[0], config.center[0])
    y1 = randint(-config.center[1], config.center[1])
    x2 = randint(-config.center[0], config.center[0])
    y2 = randint(-config.center[1], config.center[1])
    boundary = Boundary(x1, y1, x2, y2)
    boundaries.append(boundary)
    boundary.draw(screen)

raySource = RaySource(10)

# Flip the display
pygame.display.flip()


# Game loop
running = True
while running:
    pygame.time.delay(10)
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x, y = pygame.mouse.get_pos()
    x -= config.center[0]
    y = config.center[1] - y
    screen.fill(config.black)

    raySource.updateOrigin(x, y)
    raySource.draw(screen)

    for boundary in boundaries:
        boundary.draw(screen)

    pygame.display.update()

# Done! Time to quit.
pygame.quit()