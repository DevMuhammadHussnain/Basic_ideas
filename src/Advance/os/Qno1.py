"""
Qno1 - File Organizer (os)

Organize files in a folder by extension.

Difficult words:
- organize: arrange things in order
- extension: ending part of a file name (like .txt, .jpg)
- directory: folder
"""

import os


def organize_by_extension(target_folder: str) -> None:
    if not os.path.isdir(target_folder):
        print(f"Folder not found: {target_folder}")
        return

    for name in os.listdir(target_folder):
        source_path = os.path.join(target_folder, name)

        # Skip directories; only move files.
        if not os.path.isfile(source_path):
            continue

        _, ext = os.path.splitext(name)
        ext = ext.lower().lstrip(".")
        folder_name = ext if ext else "no_extension"

        dest_folder = os.path.join(target_folder, folder_name)
        os.makedirs(dest_folder, exist_ok=True)

        dest_path = os.path.join(dest_folder, name)

        # Rename works like move when target is in another folder.
        if not os.path.exists(dest_path):
            os.rename(source_path, dest_path)
            print(f"Moved: {name} -> {folder_name}/")
        else:
            print(f"Skipped (already exists): {dest_path}")


if __name__ == "__main__":
    folder = input("Enter folder path to organize: ").strip()
    organize_by_extension(folder)
