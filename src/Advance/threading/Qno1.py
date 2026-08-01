"""
Qno1 - Threaded Web Scraper (simulation)

Difficult words:
- scraper: program that collects data from web pages
"""

import threading
import time


def fetch(url: str) -> None:
    print(f"Fetching {url}...")
    time.sleep(1)
    print(f"Done {url}")


def main() -> None:
    urls = ["page1", "page2", "page3"]
    threads = [threading.Thread(target=fetch, args=(u,)) for u in urls]

    for t in threads:
        t.start()
    for t in threads:
        t.join()


if __name__ == "__main__":
    main()
