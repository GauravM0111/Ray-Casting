from random import randint
import pygame
from boundary import Boundary
from configurations import Configuration
from raySource import RaySource

# global variables
boundaries = []
config = Configuration()
timeDelay = 0
startAngle = 0

# boundary properties
numBoundaries = 5

# ray source properties
raySourceAngleOffset = 1
fovAngle = 45
velocity = 5
turnVelocity = 3
xPos = config.center2D[0]   # starting x coordinate
yPos = config.center2D[1]   # starting y coordinate

# initializes game
pygame.init()

# Set up the drawing window (surface object)
screen = pygame.display.set_mode([config.displayLength2D + config.displayLength3D, config.displayHeight])

# set up boundaries
for i in range(numBoundaries):
    x1 = randint(0, config.displayLength2D)
    y1 = randint(0, config.displayHeight)
    x2 = randint(0, config.displayLength2D)
    y2 = randint(0, config.displayHeight)
    boundary = Boundary(x1, y1, x2, y2)
    boundaries.append(boundary)

lbond = Boundary(config.outerBoundaryOffset, config.outerBoundaryOffset, config.outerBoundaryOffset, config.displayHeight-config.outerBoundaryOffset)
rbond2D = Boundary(config.displayLength2D-config.outerBoundaryOffset, config.outerBoundaryOffset, config.displayLength2D-config.outerBoundaryOffset, config.displayHeight-config.outerBoundaryOffset)
rbond3D = Boundary(config.displayFullLength-config.outerBoundaryOffset, config.outerBoundaryOffset, config.displayFullLength-config.outerBoundaryOffset, config.displayHeight-config.outerBoundaryOffset)
bbond = Boundary(config.outerBoundaryOffset, config.displayHeight-config.outerBoundaryOffset, config.displayFullLength-config.outerBoundaryOffset, config.displayHeight-config.outerBoundaryOffset)
tbond = Boundary(config.outerBoundaryOffset, config.outerBoundaryOffset, config.displayFullLength-config.outerBoundaryOffset, config.outerBoundaryOffset)
boundaries.append(lbond)
boundaries.append(rbond2D)
boundaries.append(rbond3D)
boundaries.append(bbond)
boundaries.append(tbond)

for boundary in boundaries:
    boundary.draw(screen)

# initialize ray source
raySource = RaySource(raySourceAngleOffset, coneAngle=fovAngle, startAngle=startAngle ,origin=(xPos, yPos))

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

    # 2D
    # movement
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_w] and yPos >= (config.outerBoundaryOffset + velocity):
        yPos -= velocity
    if key_input[pygame.K_a] and xPos >= (config.outerBoundaryOffset + velocity):
        xPos -= velocity
    if key_input[pygame.K_s] and yPos <= (config.displayHeight - (config.outerBoundaryOffset + velocity)):
        yPos += velocity
    if key_input[pygame.K_d] and xPos <= (config.displayLength2D - (config.outerBoundaryOffset + velocity)):
        xPos += velocity
        
    # rotation
    if key_input[pygame.K_RIGHT]:
        startAngle -= turnVelocity
    if key_input[pygame.K_LEFT]:
        startAngle += turnVelocity
        
    screen.fill(config.black)

    # draw the boundaries
    for boundary in boundaries:
        boundary.draw(screen)

    # update ray source position and draw
    raySource.updateOrigin(xPos, yPos)
    raySource.updateStartAngle(startAngle)
    raySource.draw(screen, boundaries)

    pygame.display.update()

# Done! Time to quit.
pygame.quit()