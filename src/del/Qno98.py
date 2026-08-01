"""
Qno.98: Use del to remove an object from a set.

Difficult words:
- set: unordered unique-item collection.
"""

colors = {"red", "green", "blue"}
colors_list = list(colors)
del colors_list[0]
colors = set(colors_list)
print(colors)
