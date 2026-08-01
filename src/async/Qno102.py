"""
Qno.102: Read a file asynchronously to avoid blocking the program.

Difficult words:
- blocking: when one task stops others from running.
- asynchronously: in non-blocking way.
"""

import asyncio


def read_file_sync(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


async def read_file_async(path):
    try:
        content = await asyncio.to_thread(read_file_sync, path)
        print("File content:\n", content)
    except FileNotFoundError:
        print("File not found:", path)


asyncio.run(read_file_async("sample.txt"))
