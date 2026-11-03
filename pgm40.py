square = lambda s: s * s
rectangle = lambda l, b: l * b
triangle = lambda b, h: 0.5 * b * h
s = float(input("Enter the side of square: "))
l = float(input("Enter the length of rectangle: "))
b = float(input("Enter the breadth of rectangle: "))
base = float(input("Enter the base of triangle: "))
h = float(input("Enter the height of triangle: "))
print("Area of Square:", square(s))
print("Area of Rectangle:", rectangle(l, b))
print("Area of Triangle:", triangle(base, h))
