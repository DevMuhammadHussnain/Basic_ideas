"""
Qno10 - Coroutine Timeout and cancellation

Difficult words:
- timeout: maximum allowed time
- cancellation: stop a running task
"""

import asyncio


async def long_task() -> str:
    await asyncio.sleep(3)
    return "Finished"


async def main() -> None:
    try:
        result = await asyncio.wait_for(long_task(), timeout=1.0)
        print(result)
    except asyncio.TimeoutError:
        print("Task timed out and was cancelled.")


if __name__ == "__main__":
    asyncio.run(main())
