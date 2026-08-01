"""
Qno2 - Directory Tree Viewer (os)

Print a visual tree of a folder.

Difficult words:
- visual: related to seeing
- tree: hierarchical structure like branches
- recursion: a function calling itself
"""

import os


def print_tree(path: str, prefix: str = "") -> None:
    if not os.path.exists(path):
        print(f"Path not found: {path}")
        return

    items = sorted(os.listdir(path))
    for index, item in enumerate(items):
        item_path = os.path.join(path, item)
        is_last = index == len(items) - 1
        connector = "└── " if is_last else "├── "
        print(prefix + connector + item)

        if os.path.isdir(item_path):
            extension = "    " if is_last else "│   "
            print_tree(item_path, prefix + extension)


if __name__ == "__main__":
    root = input("Enter root folder path: ").strip()
    print(root)
    print_tree(root)
