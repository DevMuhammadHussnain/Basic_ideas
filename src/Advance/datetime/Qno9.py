"""
Qno9 - Event Scheduler (datetime)

Schedule a simple one-time message at target date-time.

Difficult words:
- scheduler: system that plans execution time
- trigger: start an action when condition is met
- polling: repeated checking in a loop
"""

from datetime import datetime
import time


if __name__ == "__main__":
    text = input("Run at (YYYY-MM-DD HH:MM:SS): ").strip()
    message = input("Message: ").strip() or "Scheduled task executed"

    try:
        target = datetime.strptime(text, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        print("Invalid date-time format.")
        raise SystemExit(1)

    print("Waiting...")
    while datetime.now() < target:
        time.sleep(0.5)

    print(message)
