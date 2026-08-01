"""
Qno3 - Thread Pool

Difficult words:
- worker: thread that performs a job
- pool: managed collection/group
"""

from concurrent.futures import ThreadPoolExecutor
import time


def work(n: int) -> str:
    time.sleep(0.5)
    return f"Task {n} done"


def main() -> None:
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(work, [1, 2, 3, 4, 5]))
    print("\n".join(results))


if __name__ == "__main__":
    main()
