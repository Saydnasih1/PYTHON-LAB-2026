class Publisher:
    def __init__(self, pid, pname):
        self.pid = pid
        self.pname = pname

    def display(self):
        print("Publisher Name:", self.pname)

class Book(Publisher):
    def __init__(self, pid, pname, title, author):
        super().__init__(pid, pname)
        self.title = title
        self.author = author

class Python(Book):
    def __init__(self, pid, pname, title, author, price, pages):
        super().__init__(pid, pname, title, author)
        self.price = price
        self.pages = pages

    def display(self):
        print("\n--- Book Details ---")
        print("Publisher ID:", self.pid)
        print("Publisher Name:", self.pname)
        print("Book Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("No. of Pages:", self.pages)

pid = input("Enter Publisher ID: ")
pname = input("Enter Publisher Name: ")
title = input("Enter Book Title: ")
author = input("Enter Author Name: ")
price = float(input("Enter Price: "))
pages = int(input("Enter Number of Pages: "))

p = Python(pid, pname, title, author, price, pages)
p.display()
