"""
Qno1 - Simple HTTP Server

Difficult words:
- server: program that serves data to clients
"""

from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello from simple HTTP server")


def main() -> None:
    server = HTTPServer(("127.0.0.1", 8000), SimpleHandler)
    print("Serving on http://127.0.0.1:8000")
    server.server_close()


if __name__ == "__main__":
    main()
