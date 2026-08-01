"""
Qno.73: Create two variables with same value and check if they point to same object.

Difficult words:
- object: data instance in memory.
- reference: pointer-like link to object.
"""

a = [1, 2, 3]
b = a

print("a == b:", a == b)  # same content
print("a is b:", a is b)  # same object
