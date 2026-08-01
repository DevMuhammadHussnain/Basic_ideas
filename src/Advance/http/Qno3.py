"""
Qno3 - Web API Client

Difficult words:
- API: interface for programs to communicate
"""

from urllib.request import urlopen


def main() -> None:
    url = "http://example.com"
    with urlopen(url, timeout=5) as response:
        data = response.read(120)
        print("Status:", response.status)
        print("First bytes:", data)


if __name__ == "__main__":
    main()
