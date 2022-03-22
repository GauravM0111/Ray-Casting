import pygame
from configurations import Configuration
from ray import Ray

config = Configuration()

class RaySource:
    def __init__(self, angleOffset, coneAngle=360, startAngle=0, origin=(0, 0)):
        self.angleOffset = angleOffset
        self.origin = origin
        self.coneAngle = coneAngle
        self.startAngle = startAngle

    def draw(self, surface, boundaries):
        pygame.draw.circle(surface, config.red, self.origin, 7)

        for i in range(self.startAngle, self.startAngle + self.coneAngle, self.angleOffset):
            ray = Ray(i, self.origin)
            ray.draw(surface, boundaries)

    def updateOrigin(self, newX, newY):
        self.origin = (newX, newY)

    def updateStartAngle(self, newStartAngle):
        self.startAngle = newStartAngle