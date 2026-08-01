"""
Qno.103: Simulate downloading files asynchronously to show speed improvement.

Difficult words:
- simulate: imitate a real process.
- concurrent: tasks running in overlapping time.
"""

import asyncio


async def download_file(file_name, delay):
    print(f"Starting download: {file_name}")
    await asyncio.sleep(delay)
    print(f"Finished download: {file_name}")


async def main():
    tasks = [
        download_file("file1.zip", 2),
        download_file("file2.zip", 1),
        download_file("file3.zip", 3),
    ]
    await asyncio.gather(*tasks)
    print("All downloads complete.")


asyncio.run(main())
