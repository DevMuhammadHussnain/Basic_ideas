"""
Qno.74: Compare different data types using is to explore memory behavior.

Difficult words:
- memory behavior: how Python stores/reuses objects.
"""

x = 100
y = 100

s1 = "hello"
s2 = "hello"

l1 = [1, 2]
l2 = [1, 2]

print("x is y:", x is y)
print("s1 is s2:", s1 is s2)
print("l1 is l2:", l1 is l2)
