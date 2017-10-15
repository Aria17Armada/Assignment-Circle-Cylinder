import math

from Cylinder import Cylinder

radius = input("Radius= ")
height = input("Height= ")
color = input("Color= ")
test = Cylinder(height, radius, color)

print("The result is= ", test.getVolume(), " with the ", color, " color")
print(math.pi)
