"""
Qno2 - Asynchronous File Downloader (simulation)

Difficult words:
- source: place from where data comes
"""

import asyncio


async def download(name: str) -> None:
    print(f"Start {name}")
    await asyncio.sleep(1)
    print(f"Done {name}")


async def main() -> None:
    await asyncio.gather(download("file1"), download("file2"), download("file3"))


if __name__ == "__main__":
    asyncio.run(main())
