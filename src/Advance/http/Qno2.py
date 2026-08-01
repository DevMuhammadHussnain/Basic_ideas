"""
Qno2 - HTTP Request Handler (GET and POST)

Difficult words:
- handler: class/function that processes requests
"""

from http.server import HTTPServer, BaseHTTPRequestHandler


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"GET received")

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"POST received: " + body)


def main() -> None:
    server = HTTPServer(("127.0.0.1", 8001), Handler)
    print("HTTP handler ready at 127.0.0.1:8001")
    server.server_close()


if __name__ == "__main__":
    main()
