"""
Qno3 - Python Version Checker (sys)

Display current Python version.

Difficult words:
- interpreter: program that runs Python code
- runtime: time when program is running
- compatible: works correctly together
"""

import sys


def show_version() -> None:
    print("Python version:")
    print(sys.version)


if __name__ == "__main__":
    show_version()
