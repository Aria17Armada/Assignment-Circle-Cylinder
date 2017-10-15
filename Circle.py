import math


class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def getRadius(self, radius):
        self.radius = radius

    def setRadius(self):
        return self.radius

    def getColor(self, color):
        self.color = color

    def setColor(self):
        return self.color

    def toString(self):
        circleRad = "Circle[Radius= " + self.radius + ", Color= " + self.color + "]"
        return circleRad

    def getArea(self):
        r = int(self.radius)
        pi = math.pi
        area = pi * (r**2)
        return area

