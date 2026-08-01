"""
Qno1 - Command-line Calculator (sys)

Take numbers and operator from command-line arguments.
Example:
python Qno1.py 10 + 5

Difficult words:
- argument: value passed to a program
- parse: read and interpret
- operand: number used in a math operation
"""

import sys


def calculate(args):
    if len(args) != 3:
        print("Usage: python Qno1.py <num1> <operator> <num2>")
        return

    a_text, op, b_text = args
    try:
        a = float(a_text)
        b = float(b_text)
    except ValueError:
        print("Numbers are invalid.")
        return

    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        if b == 0:
            print("Cannot divide by zero.")
        else:
            print(a / b)
    else:
        print("Operator must be one of: + - * /")


if __name__ == "__main__":
    calculate(sys.argv[1:])
