"""
Qno5 - Temp File Cleaner (os)

Remove common temporary files automatically.

Difficult words:
- temporary: short-term, not permanent
- pattern: repeated form or style
- caution: care to avoid danger/problem
"""

import os


def is_temp_file(filename: str) -> bool:
    temp_endings = (".tmp", ".temp", ".bak", "~")
    return filename.lower().endswith(temp_endings)


def clean_temp_files(folder: str) -> None:
    if not os.path.isdir(folder):
        print(f"Folder not found: {folder}")
        return

    removed = 0
    for root, _, files in os.walk(folder):
        for name in files:
            if is_temp_file(name):
                path = os.path.join(root, name)
                try:
                    os.remove(path)
                    removed += 1
                    print(f"Removed: {path}")
                except OSError as err:
                    print(f"Could not remove {path}: {err}")

    print(f"Done. Removed {removed} temp files.")


if __name__ == "__main__":
    target = input("Enter folder path to clean: ").strip()
    clean_temp_files(target)
