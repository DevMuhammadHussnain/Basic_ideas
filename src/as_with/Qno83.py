"""
Qno.83: Catch an exception and use as to give it a name.

Difficult words:
- exception object: error details captured in variable.
"""

try:
    x = int(input("Enter integer: "))
    print("You entered:", x)
except ValueError as err:
    print("Error message:", err)
