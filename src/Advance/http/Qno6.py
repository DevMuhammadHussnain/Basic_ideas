"""
Qno6 - Custom HTTP Headers

Difficult words:
- header: metadata sent with HTTP requests/responses
"""

from urllib.request import Request, urlopen


def main() -> None:
    req = Request("http://example.com", headers={"User-Agent": "BasicIdeasClient/1.0"})
    with urlopen(req, timeout=5) as response:
        print("Status:", response.status)
        print("Server:", response.headers.get("Server"))


if __name__ == "__main__":
    main()
