"""
Qno5 - Threaded Timer

Difficult words:
- non-blocking: does not stop other code from running
"""

import threading
import time


def timer_task(seconds: int) -> None:
    time.sleep(seconds)
    print(f"Timer of {seconds}s finished")


def main() -> None:
    t = threading.Thread(target=timer_task, args=(2,))
    t.start()

    print("Doing other work...")
    time.sleep(1)
    print("Still working...")

    t.join()


if __name__ == "__main__":
    main()
