"""
Qno9 - Periodic Task Scheduler

Difficult words:
- periodic: repeated at regular intervals
"""

import asyncio


async def periodic_task() -> None:
    for i in range(5):
        print(f"Tick {i+1}")
        await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(periodic_task())
