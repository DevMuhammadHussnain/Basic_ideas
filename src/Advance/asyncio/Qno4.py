"""
Qno4 - WebSocket Server placeholder (concept demo)

Difficult words:
- real-time: immediate communication without noticeable delay

Note: Python stdlib has no full websocket server module.
This file demonstrates async server style with streams.
"""

import asyncio


async def handle(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    writer.write(b"Hello client\n")
    await writer.drain()
    writer.close()
    await writer.wait_closed()


async def main() -> None:
    server = await asyncio.start_server(handle, "127.0.0.1", 8888)
    print("Async TCP server on 127.0.0.1:8888")
    server.close()
    await server.wait_closed()


if __name__ == "__main__":
    asyncio.run(main())
