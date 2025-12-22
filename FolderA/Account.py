class Account:
    def __init__(self):
        self.__balance=100
    def get_balance(self):
        return self.__balance
acc=Account()
print(acc.get_balance())