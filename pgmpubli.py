class Publisher:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Publisher:", self.name)


class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)
        self.title = title
        self.author = author

    def display(self):
        print("Publisher:", self.name)
        print("Title:", self.title)
        print("Author:", self.author)


class Python(Book):
    def __init__(self, name, title, author, price, pages):
        super().__init__(name, title, author)
        self.price = price
        self.pages = pages

    def display(self):
        super().display()
        print("Price:", self.price)
        print("Pages:", self.pages)


name = input("Enter publisher name: ")
title = input("Enter book title: ")
author = input("Enter author name: ")
price = float(input("Enter price: "))
pages = int(input("Enter number of pages: "))

p = Python(name, title, author, price, pages)

print("\nBOOK DETAILS")
p.display()
