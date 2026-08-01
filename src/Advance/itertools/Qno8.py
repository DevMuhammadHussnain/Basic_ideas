"""
Qno8: Running Totals
Generate a running total for a list of numbers.

Difficult words:
- running total: cumulative sum (keeps adding previous values)
- cumulative: increasing by adding each new value
"""

import itertools

numbers = [5, 10, 15, 20]
running_totals = list(itertools.accumulate(numbers))

print("Numbers:", numbers)
print("Running totals:", running_totals)
