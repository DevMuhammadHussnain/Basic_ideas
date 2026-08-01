"""
Qno4 - Disk Usage Checker (os)

Display file and folder sizes (in bytes).

Difficult words:
- disk usage: storage space being used
- bytes: basic unit of digital storage
- accumulate: collect gradually
"""

import os


def folder_size(path: str) -> int:
    total = 0
    for root, _, files in os.walk(path):
        for name in files:
            file_path = os.path.join(root, name)
            if os.path.isfile(file_path):
                total += os.path.getsize(file_path)
    return total


def show_usage(path: str) -> None:
    if not os.path.exists(path):
        print(f"Path not found: {path}")
        return

    if os.path.isfile(path):
        print(f"File: {path}")
        print(f"Size: {os.path.getsize(path)} bytes")
    else:
        print(f"Folder: {path}")
        print(f"Total size: {folder_size(path)} bytes")


if __name__ == "__main__":
    p = input("Enter file/folder path: ").strip()
    show_usage(p)
