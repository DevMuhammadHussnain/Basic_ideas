"""
Qno.87: Use nonlocal to modify outer variable inside nested loop function.

Difficult words:
- outer function: parent function.
"""

def process_items(items):
    total = 0

    def add_all():
        nonlocal total
        for item in items:
            total += item

    add_all()
    print("Total:", total)


process_items([1, 2, 3, 4])
