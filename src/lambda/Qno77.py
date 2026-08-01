"""
Qno.77: Use map() with lambda to multiply each element in a list by 2.

Difficult words:
- map: apply function to each item.
"""

nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)
