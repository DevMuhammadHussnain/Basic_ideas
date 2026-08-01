"""
Qno6 - Environment Variable Viewer (os)

Show system environment variables.

Difficult words:
- environment variable: system key-value setting
- key-value: name and associated data
- iterate: go through one by one
"""

import os


def show_env() -> None:
    for key, value in sorted(os.environ.items()):
        print(f"{key}={value}")


if __name__ == "__main__":
    show_env()
