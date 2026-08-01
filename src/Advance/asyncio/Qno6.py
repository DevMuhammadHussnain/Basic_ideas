"""
Qno6 - Asynchronous Email Sender (simulation queue)

Difficult words:
- queue: line structure where first item is processed first
"""

import asyncio


async def send_email(address: str) -> None:
    await asyncio.sleep(0.5)
    print(f"Sent email to {address}")


async def worker(q: asyncio.Queue) -> None:
    while True:
        item = await q.get()
        if item is None:
            break
        await send_email(item)


async def main() -> None:
    q: asyncio.Queue = asyncio.Queue()
    emails = ["a@example.com", "b@example.com", "c@example.com"]

    for e in emails:
        await q.put(e)
    await q.put(None)

    await worker(q)


if __name__ == "__main__":
    asyncio.run(main())
