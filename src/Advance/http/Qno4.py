"""
Qno4 - HTTP Response Status handling

Difficult words:
- status code: numeric HTTP result (200, 404, ...)
"""

from urllib.request import urlopen
from urllib.error import HTTPError, URLError


def main() -> None:
    try:
        with urlopen("http://example.com/not-found", timeout=5) as response:
            print("Status:", response.status)
    except HTTPError as e:
        print("HTTP error code:", e.code)
    except URLError as e:
        print("URL error:", e.reason)


if __name__ == "__main__":
    main()
