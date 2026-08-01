"""
Qno.86: Create a counter using nonlocal to maintain count between calls.

Difficult words:
- maintain: keep/update over time.
"""

def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


c = make_counter()
print(c())
print(c())
print(c())
