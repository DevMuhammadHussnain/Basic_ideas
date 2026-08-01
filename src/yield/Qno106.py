"""
Qno.106: Use yield to create a generator that reads lines from a file lazily.

Difficult words:
- lazily: only when needed, not all at once.
"""


def read_lines_lazy(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            yield line.rstrip("\n")


try:
    for line in read_lines_lazy("sample.txt"):
        print(line)
except FileNotFoundError:
    print("sample.txt not found")
