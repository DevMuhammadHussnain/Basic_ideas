"""
Qno6: Cartesian Product
Compute the cartesian product of multiple sequences.

Difficult words:
- cartesian product: all possible pairings/combinations across sequences
"""

import itertools

a = [1, 2]
b = ["x", "y", "z"]

product_result = list(itertools.product(a, b))

print("Sequence A:", a)
print("Sequence B:", b)
print("Cartesian Product:")
for item in product_result:
    print(item)
