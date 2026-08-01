"""
Qno7 - Redirect Server

Difficult words:
- redirect: send client to another URL
"""

from http.server import HTTPServer, BaseHTTPRequestHandler


class RedirectHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(302)
        self.send_header("Location", "https://example.com")
        self.end_headers()


def main() -> None:
    server = HTTPServer(("127.0.0.1", 8003), RedirectHandler)
    print("Redirect server on 127.0.0.1:8003")
    server.server_close()


if __name__ == "__main__":
    main()
