"""
Qno3: Infinite Counter
Create an infinite counting generator using itertools.count().

Difficult words:
- infinite: never ending
- generator: object that yields values one by one
"""

import itertools

counter = itertools.count(start=1, step=2)

print("First 10 values from infinite counter:")
for _ in range(10):
    print(next(counter))
