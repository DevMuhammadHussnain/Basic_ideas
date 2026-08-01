"""
Qno.67: Use finally to always print a message after user input.

Difficult words:
- mess up: make a mistake.
"""

try:
    num = int(input("Enter an integer: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input")
finally:
    print("Input attempt finished.")
