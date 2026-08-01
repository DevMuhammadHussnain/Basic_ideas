"""
Qno5: Group By
Group elements of a sequence by a common key using itertools.groupby().

Difficult words:
- key: rule used for grouping or sorting
"""

import itertools

words = ["apple", "ant", "banana", "bat", "cat", "car"]

# Important: groupby groups consecutive items, so sort by same key first.
words_sorted = sorted(words, key=lambda x: x[0])

print("Sorted words:", words_sorted)
print("Grouped by first letter:")
for first_letter, group in itertools.groupby(words_sorted, key=lambda x: x[0]):
    print(first_letter, list(group))
