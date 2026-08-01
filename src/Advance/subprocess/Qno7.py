"""
Qno7 - Handle Errors from failed subprocess

Difficult words:
- error code: numeric value indicating success/failure
- stderr: standard error output stream
"""

import subprocess


def main() -> None:
    result = subprocess.run(["python", "-c", "import sys; print('Oops', file=sys.stderr); sys.exit(1)"], capture_output=True, text=True)

    print("Return code:", result.returncode)
    print("STDOUT:", result.stdout.strip())
    print("STDERR:", result.stderr.strip())

    if result.returncode != 0:
        print("Command failed, handled safely.")


if __name__ == "__main__":
    main()
