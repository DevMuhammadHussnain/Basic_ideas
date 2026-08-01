"""
Qno2: Combinations Finder
Find all combinations of a given size from a list.

Difficult words:
- combination: selection of items where order does not matter
"""

import itertools

items = ["A", "B", "C", "D"]
r = 2

combs = list(itertools.combinations(items, r))

print("Items:", items)
print(f"Combinations of size {r}:")
for c in combs:
    print(c)
