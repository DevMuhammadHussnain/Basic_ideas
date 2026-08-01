"""
Qno5 - Module Import Checker (sys)

Check if a module can be imported.

Difficult words:
- availability: whether something is present
- import: load module code for use
- exception: runtime error event
"""

import sys


def can_import(module_name: str) -> bool:
    try:
        __import__(module_name)
        return True
    except Exception:
        return False


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python Qno5.py <module_name>")
    else:
        mod = sys.argv[1]
        print(f"{mod}: {'available' if can_import(mod) else 'not available'}")
