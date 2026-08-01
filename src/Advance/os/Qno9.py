"""
Qno9 - Log Archiver (os)

Move old .log files from one folder to backup folder.

Difficult words:
- archive: store for long-term keeping
- backup: safety copy
- threshold: limit value
"""

import os
import time


def archive_logs(source_folder: str, backup_folder: str, older_than_days: int = 7) -> None:
    if not os.path.isdir(source_folder):
        print(f"Source folder not found: {source_folder}")
        return

    os.makedirs(backup_folder, exist_ok=True)
    now = time.time()
    threshold_seconds = older_than_days * 24 * 60 * 60

    moved = 0
    for name in os.listdir(source_folder):
        src = os.path.join(source_folder, name)
        if os.path.isfile(src) and name.lower().endswith(".log"):
            age = now - os.path.getmtime(src)
            if age > threshold_seconds:
                dst = os.path.join(backup_folder, name)
                if not os.path.exists(dst):
                    os.rename(src, dst)
                    moved += 1
                    print(f"Archived: {name}")

    print(f"Done. Moved {moved} old log files.")


if __name__ == "__main__":
    src = input("Enter logs folder path: ").strip()
    bkp = input("Enter backup folder path: ").strip()
    days_text = input("Archive logs older than days (default 7): ").strip()
    days = int(days_text) if days_text.isdigit() else 7
    archive_logs(src, bkp, days)
