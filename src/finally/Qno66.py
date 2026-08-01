"""
Qno.66: Build a calculator that handles errors and prints "Goodbye!" in finally.

Difficult words:
- handles: manages safely.
"""

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operator (+, -, *, /): ")

    if op == "+":
        print("Result:", a + b)
    elif op == "-":
        print("Result:", a - b)
    elif op == "*":
        print("Result:", a * b)
    elif op == "/":
        print("Result:", a / b)
    else:
        print("Invalid operator")
except ValueError:
    print("Please enter valid numeric input.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Goodbye!")
