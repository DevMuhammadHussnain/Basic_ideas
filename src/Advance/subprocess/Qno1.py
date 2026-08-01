"""
Qno1 - Run External Commands using subprocess.run()

Difficult words:
- external: outside the Python program
- command: instruction given to terminal/shell
"""

import subprocess


def main() -> None:
    result = subprocess.run(["echo", "Hello from subprocess.run()!"], capture_output=True, text=True)
    print("Return code:", result.returncode)
    print("Output:", result.stdout.strip())


if __name__ == "__main__":
    main()
