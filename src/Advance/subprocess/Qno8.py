"""
Qno8 - Execute Shell Scripts from Python

Difficult words:
- shell script: file with terminal commands
"""

import os
import subprocess


def main() -> None:
    script_name = "demo_script.sh"
    script_content = "#!/bin/sh\necho 'Hello from shell script'\n"

    with open(script_name, "w", encoding="utf-8") as f:
        f.write(script_content)

    os.chmod(script_name, 0o755)
    result = subprocess.run(["sh", script_name], capture_output=True, text=True)

    print("Script output:", result.stdout.strip())


if __name__ == "__main__":
    main()
