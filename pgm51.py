class Rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b

    def perimeter(self):
        return 2 * (self.l + self.b)

r1 = Rectangle(float(input("Enter length 1: ")), float(input("Enter breadth 1: ")))
r2 = Rectangle(float(input("Enter length 2: ")), float(input("Enter breadth 2: ")))

print("Area 1:", r1.area())
print("Perimeter 1:", r1.perimeter())
print("Area 2:", r2.area())
print("Perimeter 2:", r2.perimeter())

if r1.area() > r2.area():
    print("Rectangle 1 has greater area")
elif r1.area() < r2.area():
    print("Rectangle 2 has greater area")
else:
    print("Both have equal area")
