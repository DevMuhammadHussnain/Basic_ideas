"""
Qno8 - Parallel Processing of Data

Difficult words:
- chunk: small part of a large dataset
"""

import threading


def process_chunk(chunk: list[int], out: list[int], idx: int) -> None:
    out[idx] = sum(x * x for x in chunk)


def main() -> None:
    data = list(range(1, 21))
    chunks = [data[:10], data[10:]]
    results = [0, 0]

    threads = [
        threading.Thread(target=process_chunk, args=(chunks[i], results, i))
        for i in range(2)
    ]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print("Total of squares:", sum(results))


if __name__ == "__main__":
    main()
