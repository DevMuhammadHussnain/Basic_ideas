"""
Qno1: Permutation Generator
Generate all permutations of a list.

Difficult words:
- permutation: arrangement of items in different order
"""

import itertools

items = [1, 2, 3]
perms = list(itertools.permutations(items))

print("Items:", items)
print("Permutations:")
for p in perms:
    print(p)
