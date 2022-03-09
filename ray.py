import pygame
import math
from configurations import Configuration

config = Configuration()

class Ray:
    def __init__(self, angle, length, origin=(0, 0)):
        self.angle = angle
        self.length = length
        self.origin = origin

    def draw(self, surface):
        radAngle = -math.radians(self.angle)

        x = self.length * math.cos(radAngle)
        y = self.length * math.sin(radAngle)

        origCord = (config.center[0] + self.origin[0], config.center[1] - self.origin[1])
        destCord = (x + origCord[0], y + origCord[1])
        pygame.draw.line(surface, config.white, origCord, destCord)
