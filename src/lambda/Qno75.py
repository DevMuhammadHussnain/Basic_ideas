"""
Qno.75: Use a lambda function for basic operations like addition, subtraction, etc.

Difficult words:
- lambda: small anonymous function.
- anonymous: without explicit name.
"""

add = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
div = lambda a, b: a / b if b != 0 else "Cannot divide by zero"

print("Add:", add(10, 5))
print("Sub:", sub(10, 5))
print("Mul:", mul(10, 5))
print("Div:", div(10, 5))
