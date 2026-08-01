"""
Qno.68: Divide two numbers, handle zero division, and log in finally.

Difficult words:
- log: record/message for tracking.
"""

try:
    a = float(input("Enter numerator: "))
    b = float(input("Enter denominator: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Denominator cannot be zero.")
except ValueError:
    print("Invalid numeric input.")
finally:
    print("division attempt finished")
