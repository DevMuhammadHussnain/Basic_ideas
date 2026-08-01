"""
Qno.60: Raise TypeError if someone sends a string instead of a number to a math function.

Difficult words:
- TypeError: error for wrong data type.
"""

def square_number(n):
    if not isinstance(n, (int, float)):
        raise TypeError("Expected int or float.")
    return n * n


value = input("Enter a number: ")
# Try converting to number first; if user wants to test type error, comment this conversion.
try:
    if "." in value:
        parsed = float(value)
    else:
        parsed = int(value)
    print("Square:", square_number(parsed))
except ValueError:
    # If conversion fails, pass raw string to intentionally trigger TypeError.
    try:
        print("Square:", square_number(value))
    except TypeError as e:
        print(e)
except TypeError as e:
    print(e)
