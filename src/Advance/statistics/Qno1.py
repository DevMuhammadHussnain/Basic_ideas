"""
Qno1: Mean and Median Calculator
Calculate mean, median, and mode of a dataset.

Difficult words:
- dataset: a collection of data values
- mean: average value
- median: middle value after sorting
- mode: most frequently occurring value
"""

import statistics

data = [12, 15, 18, 12, 21, 24, 12, 30]

mean_value = statistics.mean(data)
median_value = statistics.median(data)
mode_value = statistics.mode(data)

print("Data:", data)
print("Mean:", mean_value)
print("Median:", median_value)
print("Mode:", mode_value)
