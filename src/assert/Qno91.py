"""
Qno.91: Use assert to make sure user input is positive.

Difficult words:
- assert: debugging check that must be true.
"""

n = int(input("Enter a positive number: "))
assert n > 0, "Number must be positive"
print("Valid positive number")
