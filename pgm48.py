class Bank:
    def assign(self):
        self.name = input("Enter name: ")
        self.accno = input("Enter account number: ")
        self.type = input("Enter account type: ")
        self.balance = float(input("Enter balance: "))

    def deposit(self):
        amt = float(input("Enter deposit amount: "))
        self.balance += amt

    def withdraw(self):
        amt = float(input("Enter withdrawal amount: "))
        if amt <= self.balance:
            self.balance -= amt
        else:
            print("Insufficient balance!")

    def display(self):
        print("\nName:", self.name)
        print("Account Number:", self.accno)
        print("Account Type:", self.type)
        print("Balance:", self.balance)


a = Bank()
a.assign()
a.deposit()
a.withdraw()
a.display()
