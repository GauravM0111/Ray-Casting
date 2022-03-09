from configurations import Configuration
from ray import Ray

config = Configuration()

class RaySource:
    def __init__(self, angleOffset, origin=(0, 0)):
        self.angleOffset = angleOffset
        self.origin = origin
        

    def draw(self, surface, boundaries):
        for i in range(0, 360, self.angleOffset):
            ray = Ray(i, self.origin)
            ray.draw(surface, boundaries)

    def updateOrigin(self, newX, newY):
        self.origin = (newX, newY)