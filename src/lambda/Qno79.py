"""
Qno.79: Sort a dictionary by its values using sorted() and a lambda function.

Difficult words:
- dictionary: key-value data structure.
"""

marks = {"Ali": 85, "Sara": 95, "John": 75}
sorted_items = sorted(marks.items(), key=lambda kv: kv[1])
print(sorted_items)
