"""
Qno10 - Startup Script Generator (os)

Create a simple startup script based on operating system.

Difficult words:
- platform-specific: different for each operating system
- executable: a file that can be run
- shebang: first line telling which interpreter to use
"""

import os


def generate_startup_script(script_name: str = "start_app") -> None:
    os_name = os.name  # 'nt' for Windows, 'posix' for Linux/macOS

    if os_name == "nt":
        filename = f"{script_name}.bat"
        content = "@echo off\npython main.py\npause\n"
    else:
        filename = script_name + ".sh"
        content = "#!/bin/sh\npython3 main.py\n"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

    if os_name != "nt":
        # Make shell script executable (rwx for owner, rx for others).
        os.chmod(filename, 0o755)

    print(f"Created startup script: {filename}")


if __name__ == "__main__":
    name = input("Enter startup script base name (default start_app): ").strip() or "start_app"
    generate_startup_script(name)
