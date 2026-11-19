from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Polygon):
    def area(self):
        l = float(input("Enter length: "))
        b = float(input("Enter breadth: "))
        print("Rectangle Area:", l * b)

class Triangle(Polygon):
    def area(self):
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        print("Triangle Area:", 0.5 * b * h)

r = Rectangle()
r.area()

t = Triangle()
t.area()
