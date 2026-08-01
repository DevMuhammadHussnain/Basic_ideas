"""
Qno2 - Custom Error Logger (sys)

Print custom errors to stderr.

Difficult words:
- stderr: standard error output stream
- stream: flow of input/output data
- diagnostic: information about a problem
"""

import sys


def log_error(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)


if __name__ == "__main__":
    msg = " ".join(sys.argv[1:]).strip() or "Something went wrong."
    log_error(msg)
