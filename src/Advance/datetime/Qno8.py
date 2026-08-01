"""
Qno8 - Time Logger (datetime)

Log events with timestamps to a file.

Difficult words:
- event: action or occurrence
- append mode: add new text without deleting old text
- chronological: in time order
"""

from datetime import datetime


def log_event(message: str, filename: str = "events.log") -> None:
    stamp = datetime.now().isoformat(timespec="seconds")
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"[{stamp}] {message}\n")


if __name__ == "__main__":
    msg = input("Enter event message: ").strip() or "No message"
    log_event(msg)
    print("Event logged.")
