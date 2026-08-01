# Qno.50
# Try to save file in a specific directory.
# Difficult words:
# - directory: folder path
# - save: write data to storage

import os

dir_path = input("Enter directory path: ").strip()
file_name = input("Enter file name: ").strip()
content = input("Enter file content: ")

try:
    os.makedirs(dir_path, exist_ok=True)
    full_path = os.path.join(dir_path, file_name)

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)

    print("File saved at:", full_path)
except OSError as e:
    print("Error saving file:", e)
