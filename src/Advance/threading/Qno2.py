"""
Qno2 - Multithreaded File Downloader (simulation)

Difficult words:
- concurrent: happening at the same time
"""

import threading
import time


def download(name: str) -> None:
    print(f"Start download: {name}")
    time.sleep(1)
    print(f"Finished download: {name}")


def main() -> None:
    files = ["fileA", "fileB", "fileC"]
    threads = [threading.Thread(target=download, args=(f,)) for f in files]

    for t in threads:
        t.start()
    for t in threads:
        t.join()


if __name__ == "__main__":
    main()
