"""
Qno7 - Async HTTP Server

Difficult words:
- request: message from client asking server for data
- response: server reply to client
"""

import asyncio


async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    _ = await reader.read(1024)
    body = b"Hello from async server"
    headers = (
        b"HTTP/1.1 200 OK\r\n"
        b"Content-Type: text/plain\r\n"
        b"Content-Length: " + str(len(body)).encode() + b"\r\n\r\n"
    )
    writer.write(headers + body)
    await writer.drain()
    writer.close()
    await writer.wait_closed()


async def main() -> None:
    server = await asyncio.start_server(handle_client, "127.0.0.1", 8081)
    print("Serving HTTP on 127.0.0.1:8081")
    server.close()
    await server.wait_closed()


if __name__ == "__main__":
    asyncio.run(main())
