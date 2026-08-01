"""
Qno3 - Batch Renamer (os)

Rename all files in a folder with a common prefix.

Difficult words:
- batch: many items together
- prefix: text added at the start
- sequential: in increasing order
"""

import os


def batch_rename(folder: str, prefix: str) -> None:
    if not os.path.isdir(folder):
        print(f"Folder not found: {folder}")
        return

    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    files.sort()

    for i, old_name in enumerate(files, start=1):
        old_path = os.path.join(folder, old_name)
        _, ext = os.path.splitext(old_name)
        new_name = f"{prefix}_{i:03d}{ext.lower()}"
        new_path = os.path.join(folder, new_name)

        if old_path == new_path:
            continue
        if os.path.exists(new_path):
            print(f"Skipped (target exists): {new_name}")
            continue

        os.rename(old_path, new_path)
        print(f"Renamed: {old_name} -> {new_name}")


if __name__ == "__main__":
    target = input("Enter folder path: ").strip()
    pref = input("Enter new name prefix: ").strip() or "file"
    batch_rename(target, pref)
