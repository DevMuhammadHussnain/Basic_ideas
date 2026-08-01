"""
Qno6 - Shared Resource Locking

Difficult words:
- race condition: wrong result when threads update shared data unsafely
- lock: object to allow one thread at a time
"""

import threading

counter = 0
lock = threading.Lock()


def increment() -> None:
    global counter
    for _ in range(10000):
        with lock:
            counter += 1


def main() -> None:
    t1 = threading.Thread(target=increment)
    t2 = threading.Thread(target=increment)

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("Final counter:", counter)


if __name__ == "__main__":
    main()
