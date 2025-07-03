class BankAccount:
    def __init__(self,Accountbalance,balance):
        self.__balance = balance
        self.__Accountbalance =balance

    def __deposit(self, amount):
        self.__balance += amount
        return f"new balance: {self.__balance}"

    def _get_balance(self):
        return self.__balance
balance = BankAccount(1000)
Accountbalance = BankAccount(500)
print(Accountbalance._get_balance)
print(balance._get_balance())  


