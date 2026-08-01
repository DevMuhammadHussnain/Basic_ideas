"""
Qno7 - Producer Consumer using queue + threading

Difficult words:
- producer: creates data
- consumer: uses data
"""

import queue
import threading
import time


def producer(q: queue.Queue) -> None:
    for i in range(5):
        item = f"item-{i}"
        q.put(item)
        print("Produced", item)
        time.sleep(0.2)
    q.put(None)


def consumer(q: queue.Queue) -> None:
    while True:
        item = q.get()
        if item is None:
            break
        print("Consumed", item)


def main() -> None:
    q: queue.Queue = queue.Queue()
    t1 = threading.Thread(target=producer, args=(q,))
    t2 = threading.Thread(target=consumer, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == "__main__":
    main()
