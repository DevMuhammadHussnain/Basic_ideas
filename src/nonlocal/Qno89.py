"""
Qno.89: Create a function that modifies outer variables using nonlocal.

Difficult words:
- modify: change value.
"""

def outer_values():
    a = 10
    b = 20

    def changer():
        nonlocal a, b
        a += 5
        b += 10
        print("Inside changer:", a, b)

    changer()
    print("After changer:", a, b)


outer_values()
