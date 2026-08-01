"""
Qno8 - Auto Folder Creator (os)

Create a basic project folder structure quickly.

Difficult words:
- structure: organized arrangement
- scaffold: basic framework
- convention: commonly accepted pattern
"""

import os


def create_project_structure(base_path: str, project_name: str) -> None:
    project_root = os.path.join(base_path, project_name)
    folders = [
        "src",
        "tests",
        "docs",
        "data",
        os.path.join("src", "utils"),
    ]

    for folder in folders:
        full_path = os.path.join(project_root, folder)
        os.makedirs(full_path, exist_ok=True)
        print(f"Created: {full_path}")


if __name__ == "__main__":
    base = input("Enter base path: ").strip() or "."
    name = input("Enter project name: ").strip() or "my_project"
    create_project_structure(base, name)
