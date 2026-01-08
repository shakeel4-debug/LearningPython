from FolderA.BankAccount import account


class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        if amount<=self.balance:
            self.balance -= amount
            return f"Withdraw ${self.balance}.Balance"
        return "Insufficient balance"
    def get_count(self):
        return f"{self.name} has {self.balance} Balance"
account=BankAccount("Alice",100)
print(account.get_count())
account.deposit(100)
print(account.get_count())
