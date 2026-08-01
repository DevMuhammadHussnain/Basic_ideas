"""
Qno4: Circular Iteration
Use itertools.cycle() for repeating a sequence infinitely.

Difficult words:
- circular iteration: looping repeatedly over the same data
"""

import itertools

colors = ["red", "green", "blue"]
cycler = itertools.cycle(colors)

print("First 10 cycled values:")
for _ in range(10):
    print(next(cycler))
