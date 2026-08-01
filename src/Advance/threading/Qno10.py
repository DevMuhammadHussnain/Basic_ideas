"""
Qno10 - Thread Synchronization with Event

Difficult words:
- synchronization: coordinating order/timing between threads
"""

import threading
import time

ready = threading.Event()


def worker() -> None:
    print("Worker: waiting for signal...")
    ready.wait()
    print("Worker: signal received, working now.")


def main() -> None:
    t = threading.Thread(target=worker)
    t.start()

    time.sleep(1)
    print("Main: sending signal")
    ready.set()

    t.join()


if __name__ == "__main__":
    main()
