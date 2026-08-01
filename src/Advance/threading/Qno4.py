"""
Qno4 - Background Task Runner

Difficult words:
- background task: job running behind main flow
"""

import threading
import time


def background() -> None:
    for i in range(3):
        print(f"Background step {i+1}")
        time.sleep(1)


def main() -> None:
    t = threading.Thread(target=background)
    t.start()

    print("Main thread continues...")
    t.join()
    print("Background finished.")


if __name__ == "__main__":
    main()
