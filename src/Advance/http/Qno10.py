"""
Qno10 - Cookie Handling

Difficult words:
- cookie: small data saved by browser/server for state tracking
"""

from http.cookies import SimpleCookie


def main() -> None:
    cookie = SimpleCookie()
    cookie["username"] = "python_student"
    cookie["username"]["path"] = "/"

    print("Set-Cookie header:")
    print(cookie.output())

    incoming = "sessionid=abc123; theme=dark"
    parsed = SimpleCookie()
    parsed.load(incoming)

    print("Parsed cookies:")
    for key, morsel in parsed.items():
        print(key, "=", morsel.value)


if __name__ == "__main__":
    main()
