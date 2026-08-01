"""
Qno5 - File Server with http.server

Difficult words:
- share: make available to others
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler


def main() -> None:
    server = HTTPServer(("127.0.0.1", 8002), SimpleHTTPRequestHandler)
    print("File server at http://127.0.0.1:8002")
    server.server_close()


if __name__ == "__main__":
    main()
