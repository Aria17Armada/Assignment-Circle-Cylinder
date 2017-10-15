import math

from Circle import Circle


class Cylinder(Circle):
    def __init__(self, height, radius, color):
        Circle.__init__(self, radius, color)
        self.height = height

    def getHeight(self, height):
        self.height = height

    def setHeight(self):
        return self.height

    def toString(self):
        cylinderRad = "Cylinder[Radius=" + self.radius + " ,Color= " + self.color + " ,Height= " + self.height + " ]"
        return cylinderRad

    def getVolume(self):
        r = int(self.radius)
        h = int(self.height)
        pi = math.pi
        V = pi * (r ** 2) * h
        return V
