"""
Qno8 - Interactive Shell Detector (sys)

Detect whether script appears to run interactively.

Difficult words:
- interactive: user gives input while running
- shell: command-line environment
- attribute: property of an object
"""

import sys


def is_interactive() -> bool:
    # sys.ps1 usually exists in interactive mode.
    return hasattr(sys, "ps1")


if __name__ == "__main__":
    print("Interactive mode detected." if is_interactive() else "Non-interactive script mode.")
