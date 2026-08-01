"""
Qno8 - HTTPS Request Handler (client with SSL)

Difficult words:
- SSL: security layer for encrypted connection
- secure: protected from eavesdropping
"""

from urllib.request import urlopen


def main() -> None:
    with urlopen("https://example.com", timeout=5) as response:
        print("HTTPS status:", response.status)


if __name__ == "__main__":
    main()
