"""
Qno.76: Sort a list of tuples by the second item using a lambda function.

Difficult words:
- tuple: immutable collection.
- sort: arrange in order.
"""

data = [("Ali", 70), ("Sara", 90), ("John", 80)]
sorted_data = sorted(data, key=lambda item: item[1])
print(sorted_data)
