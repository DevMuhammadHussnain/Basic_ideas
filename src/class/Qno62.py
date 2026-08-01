"""
Qno.62: Create a class to simulate a bank account with deposit, withdraw, check_balance.

Difficult words:
- simulate: imitate behavior of real system.
"""

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount

    def check_balance(self):
        return self.balance


acc = BankAccount("Sara", 1000)
acc.deposit(500)
acc.withdraw(300)
print("Balance:", acc.check_balance())
