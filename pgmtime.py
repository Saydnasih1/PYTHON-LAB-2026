class Time:
    def __init__(self, h, m, s):
        self.__h = h
        self.__m = m
        self.__s = s

    def __add__(self, other):
        s = self.__s + other.__s
        m = self.__m + other.__m + s // 60
        h = self.__h + other.__h + m // 60

        return Time(h, m % 60, s % 60)

    def display(self):
        print(self.__h, ":", self.__m, ":", self.__s)


h1 = int(input("Enter first hour: "))
m1 = int(input("Enter first minute: "))
s1 = int(input("Enter first second: "))

h2 = int(input("Enter second hour: "))
m2 = int(input("Enter second minute: "))
s2 = int(input("Enter second second: "))

t1 = Time(h1, m1, s1)
t2 = Time(h2, m2, s2)

t3 = t1 + t2

print("Sum of two times:")
t3.display()
