"""
Author: Devin Lepur
Practicing very basic OOP with python
Simple bank account OOP practice with classes and 'self.' usage. Also printf
1/5/23
"""

class Account:
    def __init__(self, name):
        self.accountName = name
        self.balance = 0
        self.fees = 0
        print(f"Created account: {self.accountName}\n")
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount} into {self.accountName}")
        print(f"Resulting balance: ${self.balance}\n")

    def withdraw(self, amount):
        if(amount > self.balance):
            print("Insefficient funds, withdrawal canceled\n")
            return
        self.balance -= amount
        print(f"Withdrew ${amount} from {self.accountName}")
        print(f"Resulting balance: ${self.balance}\n")


myAccount = Account("Retirement Fund")
myAccount.deposit(10)
myAccount.withdraw(10.01)
myAccount.withdraw(7)