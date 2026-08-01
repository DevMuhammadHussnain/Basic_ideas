"""
Qno7: Chunks of Data
Split a list into fixed-size chunks using itertools.islice().

Difficult words:
- chunk: small fixed-size part of data
- islice: iterator-based slicing
"""

import itertools

data = list(range(1, 16))
chunk_size = 4

print("Data:", data)
print("Chunks:")

it = iter(data)
while True:
    chunk = list(itertools.islice(it, chunk_size))
    if not chunk:
        break
    print(chunk)
