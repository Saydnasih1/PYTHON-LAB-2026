class Rectangle:
    def __init__(self, l, w):
        self.__length = l
        self.__width = w

    def area(self):
        return self.__length * self.__width

    def __lt__(self, other):
        return self.area() < other.area()


l1 = int(input("Enter length of rectangle 1: "))
w1 = int(input("Enter width of rectangle 1: "))

l2 = int(input("Enter length of rectangle 2: "))
w2 = int(input("Enter width of rectangle 2: "))

r1 = Rectangle(l1, w1)
r2 = Rectangle(l2, w2)

if r1 < r2:
    print("Rectangle 1 has smaller area")
else:
    print("Rectangle 2 has smaller or equal area")
