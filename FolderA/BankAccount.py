from os import access


class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        return f"Deposited ${amount}. New balance is ${self.balance}"

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance-=amount
            return f"Withdrawed ${amount}. New balance is ${self.balance}"
        return "Insufficient balance"
account=BankAccount("Shakeel",100)
print(account.deposit(50))
print(account.withdraw(30))