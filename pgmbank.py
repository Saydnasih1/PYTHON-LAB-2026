class Bank:
    def __init__(self, accno, name, type, balance):
        self.accno = accno
        self.name = name
        self.type = type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def display(self):
        print("Account No:", self.accno)
        print("Name:", self.name)
        print("Account Type:", self.type)
        print("Balance:", self.balance)


a = Bank(input("Enter account number: "),
         input("Enter name: "),
         input("Enter account type: "),
         float(input("Enter balance: ")))

a.deposit(float(input("Enter deposit amount: ")))
a.withdraw(float(input("Enter withdrawal amount: ")))
a.display()
