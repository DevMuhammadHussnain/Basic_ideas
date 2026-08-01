"""
Qno9 - Basic HTTP Proxy Server (minimal)

Difficult words:
- proxy: server that forwards client requests
- route: send data through a specific path
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.request import urlopen


class ProxyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        target = "http://example.com"
        with urlopen(target, timeout=5) as resp:
            data = resp.read(200)

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(data)


def main() -> None:
    server = HTTPServer(("127.0.0.1", 8004), ProxyHandler)
    print("Proxy server on 127.0.0.1:8004")
    server.server_close()


if __name__ == "__main__":
    main()
