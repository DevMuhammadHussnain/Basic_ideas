"""
Qno8 - Async File I/O (using thread offload)

Difficult words:
- non-blocking: does not freeze event loop
- offload: move work to another thread/process
"""

import asyncio


def write_file(path: str, text: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


async def main() -> None:
    path = "async_file.txt"
    await asyncio.to_thread(write_file, path, "Async file content")
    content = await asyncio.to_thread(read_file, path)
    print(content)


if __name__ == "__main__":
    asyncio.run(main())
