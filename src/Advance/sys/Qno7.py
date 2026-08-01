"""
Qno7 - Script Timer (sys)

Use command-line argument as duration for countdown timer.

Difficult words:
- duration: length of time
- countdown: counting backward to zero
- argument: input value passed via command line
"""

import sys
import time


def timer(seconds: int) -> None:
    for remaining in range(seconds, -1, -1):
        print(f"Remaining: {remaining} sec")
        time.sleep(1)
    print("Time up!")


if __name__ == "__main__":
    if len(sys.argv) < 2 or not sys.argv[1].isdigit():
        print("Usage: python Qno7.py <seconds>")
    else:
        timer(int(sys.argv[1]))
