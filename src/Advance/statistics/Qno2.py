"""
Qno2: Standard Deviation Finder
Compute standard deviation for a list of numbers.

Difficult words:
- standard deviation: how spread out values are from the mean
- spread: how far values are from each other
"""

import statistics

numbers = [10, 12, 23, 23, 16, 23, 21, 16]
std_dev_sample = statistics.stdev(numbers)   # sample standard deviation
std_dev_population = statistics.pstdev(numbers)  # population standard deviation

print("Numbers:", numbers)
print("Sample Standard Deviation:", std_dev_sample)
print("Population Standard Deviation:", std_dev_population)
