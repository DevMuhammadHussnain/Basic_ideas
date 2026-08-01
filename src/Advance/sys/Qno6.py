"""
Qno6 - Memory Usage Tracker (sys)

Use sys.getsizeof() to inspect object sizes.

Difficult words:
- inspect: examine carefully
- object: data item in Python
- approximate: close estimate, not exact total memory
"""

import sys


def show_sizes() -> None:
    samples = {
        "int": 123,
        "float": 3.14,
        "string": "hello",
        "list": [1, 2, 3],
        "dict": {"a": 1, "b": 2},
        "tuple": (1, 2, 3),
        "set": {1, 2, 3},
    }

    for name, obj in samples.items():
        print(f"{name}: {sys.getsizeof(obj)} bytes")


if __name__ == "__main__":
    show_sizes()
