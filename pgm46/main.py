
# Selective import of modules
from graphics import rectangle, circle

# Import all functions from cuboid
from graphics.graphics_3D.cuboid import *

# Import sphere as a module
import graphics.graphics_3D.sphere as sphere


# Rectangle
print("\n--- RECTANGLE ---")
l = float(input("Enter length: "))
b = float(input("Enter breadth: "))

print("Area of Rectangle:", rectangle.area(l, b))
print("Perimeter of Rectangle:", rectangle.perimeter(l, b))


# Circle
print("\n--- CIRCLE ---")
r = float(input("Enter radius: "))

print("Area of Circle:", circle.area(r))
print("Perimeter of Circle:", circle.perimeter(r))


# Cuboid
print("\n--- CUBOID ---")
l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
h = float(input("Enter height: "))

print("Surface Area of Cuboid:", area(l, b, h))
print("Volume of Cuboid:", volume(l, b, h))


# Sphere
print("\n--- SPHERE ---")
r = float(input("Enter radius: "))

print("Surface Area of Sphere:", sphere.area(r))
print("Volume of Sphere:", sphere.volume(r))

