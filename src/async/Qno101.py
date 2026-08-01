"""
Qno.101: Write an async function that waits for a specified time before completing.

Difficult words:
- async: allows non-blocking concurrent tasks.
- await: pause here until awaited task finishes.
"""

import asyncio


async def wait_and_finish(seconds):
    print(f"Waiting for {seconds} seconds...")
    await asyncio.sleep(seconds)
    print("Task completed.")


asyncio.run(wait_and_finish(2))
