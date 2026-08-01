"""
Qno9 - Parallel Task Execution with subprocess

Difficult words:
- parallel: multiple tasks running at same time
"""

import subprocess


def main() -> None:
    processes = [
        subprocess.Popen(["python", "-c", "import time; time.sleep(1); print('Task 1 done')"]),
        subprocess.Popen(["python", "-c", "import time; time.sleep(2); print('Task 2 done')"]),
        subprocess.Popen(["python", "-c", "import time; time.sleep(3); print('Task 3 done')"]),
    ]

    for proc in processes:
        proc.wait()

    print("All subprocess tasks completed.")


if __name__ == "__main__":
    main()
