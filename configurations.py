class Configuration:
    def __init__(self):
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255,0,0)
        self.outerBoundaryOffset = 10
        self.displayLength2D = 700
        self.displayLength3D = 700
        self.displayFullLength = self.displayLength2D + self.displayLength3D
        self.displayHeight = 700
        self.center2D = [self.displayLength2D/2, self.displayHeight/2]
        self.center3D = [self.displayLength2D + self.displayLength3D/2, self.displayHeight/2]
        self.start3D = self.displayLength2D-self.outerBoundaryOffset