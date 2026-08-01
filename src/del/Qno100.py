"""
Qno.100: Use del to remove an object from a set.

Difficult words:
- remove: delete an element.
"""

animals = {"cat", "dog", "bird"}
animals_list = list(animals)
del animals_list[-1]
animals = set(animals_list)
print(animals)
