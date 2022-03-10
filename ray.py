from boundary import Boundary
import numpy as np
import pygame
import math
from configurations import Configuration

config = Configuration()


class Ray:
    def __init__(self, angle, origin=(0, 0)):
        self.angle = -math.radians(angle)
        self.origin = origin

    def closestHitDistance(self, boundaries):
        closestDist = max(config.displaySize[0], config.displaySize[1]) * 2.0
        closestX = (closestDist * np.cos(self.angle)) + self.origin[0]
        closestY = (closestDist * np.sin(self.angle)) + self.origin[1]

        x1 = self.origin[0]
        y1 = self.origin[1]

        for boundary in boundaries:
            denom = np.linalg.det(np.array([[(x1 - closestX), (boundary.x1 - boundary.x2)], [(y1 - closestY), (boundary.y1 - boundary.y2)]]))
            if math.fabs(denom) < 0.1:
                continue

            t = np.linalg.det(np.array([[(x1 - boundary.x1), (boundary.x1 - boundary.x2)], [(y1 - boundary.y1), (boundary.y1 - boundary.y2)]])) / denom
            if t < 0.0 or t > 1.0:
                continue

            u = np.linalg.det(np.array([[(x1 - boundary.x1), (x1 - closestX)], [(y1 - boundary.y1), (y1 - closestY)]])) / denom
            if u < 0.0 or u > 1.0:
                continue

            intX = x1 + (t*(closestX-x1))
            intY = y1 + (t*(closestY-y1))

            distFromOrig = math.sqrt(((intX - x1) ** 2) + ((intY - y1) ** 2))

            if distFromOrig < closestDist:
                closestDist = distFromOrig
                closestX = intX
                closestY = intY

        return closestDist

    def draw(self, surface, boundaries):
        closestDist = self.closestHitDistance(boundaries)

        x = closestDist * np.cos(self.angle)
        y = closestDist * np.sin(self.angle)
        destCord = (x + self.origin[0], y + self.origin[1])

        pygame.draw.line(surface, config.white, self.origin, destCord)