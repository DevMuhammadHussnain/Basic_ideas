"""
Qno9: Collapsing Sequences
Collapse a sequence by skipping elements using itertools.dropwhile().

Difficult words:
- collapse: reduce by removing/skipping
- dropwhile: skip items while condition is true
"""

import itertools

data = [1, 2, 3, 0, 4, 5]

# Skip values while they are less than 3
result = list(itertools.dropwhile(lambda x: x < 3, data))

print("Original data:", data)
print("After dropwhile(x < 3):", result)
