"""
Qno7 - Permission Modifier (os)

Change read/write/execute permissions using numeric mode.

Difficult words:
- permission: allowed action
- execute: run a program/file
- octal: base-8 number system (e.g., 755)
"""

import os


def change_permission(path: str, mode_text: str) -> None:
    if not os.path.exists(path):
        print(f"Path not found: {path}")
        return

    try:
        mode = int(mode_text, 8)  # parse as octal
        os.chmod(path, mode)
        print(f"Permissions updated for {path} to {mode_text}")
    except ValueError:
        print("Invalid mode. Use octal like 644 or 755.")
    except OSError as err:
        print(f"Could not change permissions: {err}")


if __name__ == "__main__":
    p = input("Enter file/folder path: ").strip()
    m = input("Enter mode (octal, e.g., 644): ").strip()
    change_permission(p, m)
