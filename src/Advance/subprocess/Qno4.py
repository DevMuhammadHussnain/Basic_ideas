"""
Qno4 - File Operations via command-line tools

Difficult words:
- manipulate: change/edit data or files
"""

import os
import subprocess


def main() -> None:
    file_name = "sample_subprocess_file.txt"
    subprocess.run(["python", "-c", f"open('{file_name}','w').write('Created by subprocess')"], check=True)

    print("File created?", os.path.exists(file_name))
    if os.path.exists(file_name):
        with open(file_name, "r", encoding="utf-8") as f:
            print("File content:", f.read())


if __name__ == "__main__":
    main()
