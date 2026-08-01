"""
Qno10: Slice Generator
Create slices of data based on a condition using itertools.compress().

Difficult words:
- selector: True/False mask used to choose elements
- compress: filter data by selectors
"""

import itertools

data = ["A", "B", "C", "D", "E"]
selectors = [1, 0, 1, 0, 1]  # truthy values keep items

filtered = list(itertools.compress(data, selectors))

print("Data:", data)
print("Selectors:", selectors)
print("Compressed/Filtered result:", filtered)
