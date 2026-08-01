"""
Qno.84: Raise custom exception and use as to capture it.

Difficult words:
- debugging: finding and fixing bugs.
"""

class CustomError(Exception):
    pass


def check_value(v):
    if v < 0:
        raise CustomError("Negative value not allowed")


try:
    n = int(input("Enter number: "))
    check_value(n)
    print("Valid value")
except CustomError as e:
    print("Caught custom error:", e)
