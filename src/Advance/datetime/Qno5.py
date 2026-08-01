"""
Qno5 - Countdown Timer (datetime)

Show remaining time until a future date-time.

Difficult words:
- countdown: decreasing remaining time
- future: time that has not happened yet
- interval: amount between two times
"""

from datetime import datetime
import time


if __name__ == "__main__":
    text = input("Enter future date-time (YYYY-MM-DD HH:MM:SS): ").strip()
    try:
        target = datetime.strptime(text, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        print("Invalid format.")
        raise SystemExit(1)

    while True:
        now = datetime.now()
        remaining = target - now
        seconds = int(remaining.total_seconds())
        if seconds <= 0:
            print("Time reached!")
            break
        print(f"Remaining: {remaining}", end="\r")
        time.sleep(1)
