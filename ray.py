import numpy as np
import pygame
import math
from configurations import Configuration

config = Configuration()


def onSegment(p, q, r):
    if ( (q[0] <= max(p[0], r[0])) and (q[0] >= min(p[0], r[0])) and
           (q[1] <= max(p[1], r[1])) and (q[1] >= min(p[1], r[1]))):
        return True
    return False

def orientation(p, q, r):
    # to find the orientation of an ordered triplet (p,q,r)
    # function returns the following values:
    # 0 : Collinear points
    # 1 : Clockwise points
    # 2 : Counterclockwise
     
    val = (float(q[1] - p[1]) * (r[0] - q[0])) - (float(q[0] - p[0]) * (r[1] - q[1]))
    if (val > 0):
         
        # Clockwise orientation
        return 1
    elif (val < 0):
         
        # Counterclockwise orientation
        return 2
    else:
         
        # Collinear orientation
        return 0


def doIntersect(p1,q1,p2,q2):
     
    # Find the 4 orientations required for
    # the general and special cases
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
 
    # General case
    if ((o1 != o2) and (o3 != o4)):
        return True
 
    # Special Cases
 
    # p1 , q1 and p2 are collinear and p2 lies on segment p1q1
    if ((o1 == 0) and onSegment(p1, p2, q1)):
        return True
 
    # p1 , q1 and q2 are collinear and q2 lies on segment p1q1
    if ((o2 == 0) and onSegment(p1, q2, q1)):
        return True
 
    # p2 , q2 and p1 are collinear and p1 lies on segment p2q2
    if ((o3 == 0) and onSegment(p2, p1, q2)):
        return True
 
    # p2 , q2 and q1 are collinear and q1 lies on segment p2q2
    if ((o4 == 0) and onSegment(p2, q1, q2)):
        return True
 
    # If none of the cases
    return False

class Ray:
    def __init__(self, angle, origin=(0, 0)):
        self.angle = -math.radians(angle)
        self.origin = origin

    def closestHitDistance(self, boundaries, surface):
        closestDist = max(config.displaySize[0], config.displaySize[1]) * 2.0
        closestX = (closestDist * np.cos(self.angle)) + self.origin[0]
        closestY = (closestDist * np.sin(self.angle)) + self.origin[1]

        x1 = self.origin[0]
        y1 = self.origin[1]

        pointXDet = np.linalg.det(np.array([[x1, 1], [closestX, 1]]))
        pointYDet = np.linalg.det(np.array([[y1, 1], [closestY, 1]]))
        pointXYDet = np.linalg.det(np.array([[x1, y1], [closestX, closestY]]))

        for boundary in boundaries:
            if not doIntersect([x1, y1], [closestX, closestY], [boundary.x1, boundary.y1], [boundary.x2, boundary.y2]):
                continue

            boundXDet = np.linalg.det(np.array([[boundary.x1, 1], [boundary.x2, 1]]))
            boundYDet = np.linalg.det(np.array([[boundary.y1, 1], [boundary.y2, 1]]))

            denom = np.linalg.det(np.array([[pointXDet, pointYDet], [boundXDet, boundYDet]]))
            if math.fabs(denom) < 0.1:
                continue

            boundXYDet = np.linalg.det(np.array([[boundary.x1, boundary.y1], [boundary.x2, boundary.y2]]))

            intX = np.linalg.det(np.array([[pointXYDet, pointXDet], [boundXYDet, boundXDet]])) / denom
            intY = np.linalg.det(np.array([[pointXYDet, pointYDet], [boundXYDet, boundYDet]])) / denom

            distFromOrig = math.sqrt(((intX - x1) ** 2) + ((intY - y1) ** 2))

            if distFromOrig < closestDist:
                closestDist = distFromOrig
                closestX = intX
                closestY = intY

        return closestDist

    def draw(self, surface, boundaries):
        closestDist = self.closestHitDistance(boundaries, surface)

        x = closestDist * np.cos(self.angle)
        y = closestDist * np.sin(self.angle)
        destCord = (x + self.origin[0], y + self.origin[1])

        #pygame.draw.circle(surface, (255, 0, 0), destCord, 7)
        pygame.draw.line(surface, config.white, self.origin, destCord)