"""
Qno9 - Command Logger (sys)

Save all command-line arguments to a file.

Difficult words:
- auditing: checking records for review
- persist: keep data stored
- timestamp: date/time mark
"""

import sys
from datetime import datetime


def log_arguments(log_file: str = "command_log.txt") -> None:
    now = datetime.now().isoformat(timespec="seconds")
    args = sys.argv[1:]
    with open(log_file, "a", encoding="utf-8") as file:
        file.write(f"[{now}] args={args}\n")
    print(f"Logged {len(args)} argument(s) to {log_file}")


if __name__ == "__main__":
    log_arguments()
