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
        self.num_rays = coneAngle / angleOffset
        self.rect_width = config.displayLength3D / self.num_rays

    def draw(self, surface, boundaries):
        pygame.draw.circle(surface, config.red, self.origin, 7)
        ray_num = 0
        
        for i in range(self.startAngle, self.startAngle + self.coneAngle, self.angleOffset):
            # 2D
            ray = Ray(i, self.origin)
            ray.draw(surface, boundaries)

            # 3D
            hit_dist = int(ray.getClosestHitDist())
            bright_scaling = hit_dist
            height_scaling = hit_dist

            if (bright_scaling > 255):
                bright_scaling = 255
            if (height_scaling > config.displayHeight):
                height_scaling = config.displayHeight

            pygame.draw.rect(surface, (255-bright_scaling, 255-bright_scaling, 255-bright_scaling), pygame.Rect(config.start3D + (ray_num * self.rect_width), (config.outerBoundaryOffset + (height_scaling/2)), self.rect_width, (config.displayHeight-height_scaling)))

            ray_num += 1

    def updateOrigin(self, newX, newY):
        self.origin = (newX, newY)

    def updateStartAngle(self, newStartAngle):
        self.startAngle = newStartAngle