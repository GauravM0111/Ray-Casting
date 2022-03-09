from configurations import Configuration
from ray import Ray

config = Configuration()

class RaySource:
    def __init__(self, angleOffset, origin=(0, 0)):
        self.angleOffset = angleOffset
        self.origin = origin
        self.rays = []

    def draw(self, surface):
        for i in range(0, 360, self.angleOffset):
            ray = Ray(i, 50, self.origin)
            self.rays.append(ray)
            ray.draw(surface)

    def updateOrigin(self, newX, newY):
        self.origin = (newX, newY)