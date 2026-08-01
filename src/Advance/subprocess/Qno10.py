"""
Qno10 - External Command Timer

Difficult words:
- execution time: total time a command takes to finish
"""

import subprocess
import time


def main() -> None:
    start = time.perf_counter()
    subprocess.run(["python", "-c", "import time; time.sleep(1.5); print('timed command')"], check=True)
    end = time.perf_counter()

    print(f"Execution time: {end - start:.3f} seconds")


if __name__ == "__main__":
    main()
