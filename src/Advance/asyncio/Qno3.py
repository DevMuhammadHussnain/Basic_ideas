"""
Qno3 - Background Task Scheduler

Difficult words:
- scheduler: system that plans when tasks run
"""

import asyncio


async def background_task() -> None:
    for i in range(3):
        await asyncio.sleep(1)
        print(f"Background step {i+1}")


async def main() -> None:
    task = asyncio.create_task(background_task())

    for i in range(2):
        print("Main doing work...")
        await asyncio.sleep(0.7)

    await task


if __name__ == "__main__":
    asyncio.run(main())
