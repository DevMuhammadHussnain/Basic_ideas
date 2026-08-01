"""
Qno4 - Path Explorer (sys)

Explore Python import paths and optionally add one.

Difficult words:
- import path: folder list where Python searches modules
- append: add at the end
- runtime: while program is running
"""

import sys


def show_paths() -> None:
    for i, p in enumerate(sys.path, start=1):
        print(f"{i}. {p}")


def add_path(new_path: str) -> None:
    if new_path and new_path not in sys.path:
        sys.path.append(new_path)
        print(f"Added to sys.path: {new_path}")


if __name__ == "__main__":
    print("Current sys.path:")
    show_paths()
    extra = input("Enter a path to append (or blank to skip): ").strip()
    add_path(extra)
