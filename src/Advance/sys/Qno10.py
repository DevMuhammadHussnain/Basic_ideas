"""
Qno10 - Exit Code Tester (sys)

Exit with a custom code.

Difficult words:
- exit code: numeric status returned when script ends
- convention: common rule (0 means success)
- externally: from another script or shell
"""

import sys


def exit_with_code(code_text: str) -> None:
    try:
        code = int(code_text)
    except ValueError:
        print("Invalid code. Use an integer.")
        sys.exit(2)

    print(f"Exiting with code {code}")
    sys.exit(code)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python Qno10.py <exit_code>")
        sys.exit(1)
    exit_with_code(sys.argv[1])
