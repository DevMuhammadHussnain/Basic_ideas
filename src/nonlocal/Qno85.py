"""
Qno.85: Use nonlocal to modify a variable in nested function.

Difficult words:
- nonlocal: refers to outer (not global) variable.
- nested: function inside another function.
"""

def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        print("Count:", count)

    inner()
    inner()


outer()
