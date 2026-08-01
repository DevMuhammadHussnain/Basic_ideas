"""
Qno.90: Create a function that retains state using nonlocal and returns in different calls.

Difficult words:
- retain state: remember previous value between calls.
"""

def accumulator():
    total = 0

    def add(n):
        nonlocal total
        total += n
        return total

    return add


acc = accumulator()
print(acc(5))
print(acc(10))
print(acc(-3))
