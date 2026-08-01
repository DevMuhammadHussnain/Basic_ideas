"""
Qno5 - Command Argument Parser for subprocess target

Difficult words:
- parse: analyze text/options into structured values
"""

import argparse
import subprocess


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a subprocess command")
    parser.add_argument("--name", default="World", help="Name to greet")
    args = parser.parse_args()

    code = f"print('Hello, {args.name}!')"
    result = subprocess.run(["python", "-c", code], capture_output=True, text=True)
    print(result.stdout.strip())


if __name__ == "__main__":
    main()
