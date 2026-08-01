"""
Qno5 - Async Database Query (simulation)

Difficult words:
- query: request for data
- blocking: stops other tasks until completion
"""

import asyncio


async def fake_db_query(sql: str) -> str:
    await asyncio.sleep(1)
    return f"Result for: {sql}"


async def main() -> None:
    result = await fake_db_query("SELECT * FROM users")
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
