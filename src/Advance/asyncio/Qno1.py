"""
Qno1 - Simple Asynchronous Web Scraper (simulation)

Difficult words:
- asynchronous: tasks can run while waiting for others
"""

import asyncio


async def fetch(page: str) -> str:
    await asyncio.sleep(1)
    return f"Data from {page}"


async def main() -> None:
    pages = ["page1", "page2", "page3"]
    results = await asyncio.gather(*(fetch(p) for p in pages))
    for r in results:
        print(r)


if __name__ == "__main__":
    asyncio.run(main())
