"""
Qno9 - GUI Event Loop style simulation with threading

Difficult words:
- event loop: repeated cycle handling events/tasks
"""

import threading
import time


def fake_gui_loop() -> None:
    for i in range(5):
        print(f"GUI tick {i}")
        time.sleep(0.5)


def background_work() -> None:
    for i in range(3):
        print(f"Worker step {i}")
        time.sleep(0.7)


def main() -> None:
    worker = threading.Thread(target=background_work)
    worker.start()

    fake_gui_loop()
    worker.join()


if __name__ == "__main__":
    main()
