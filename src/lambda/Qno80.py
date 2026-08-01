"""
Qno.80: Find smallest or largest number in a list using min()/max() with lambda.

Difficult words:
- smallest/largest: minimum/maximum.
"""

nums = [12, 3, 45, 7, 19]
smallest = min(nums, key=lambda x: x)
largest = max(nums, key=lambda x: x)

print("Smallest:", smallest)
print("Largest:", largest)
