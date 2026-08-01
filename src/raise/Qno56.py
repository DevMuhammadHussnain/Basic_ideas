"""
Qno.56: Raise an exception if someone tries to withdraw more than balance.

Difficult words:
- withdraw: take money out.
- balance: available money amount.
"""

def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance.")
    return balance - amount


b = float(input("Enter current balance: "))
a = float(input("Enter withdraw amount: "))

try:
    new_balance = withdraw(b, a)
    print("New balance:", new_balance)
except ValueError as e:
    print(e)
