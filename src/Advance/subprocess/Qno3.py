"""
Qno3 - Process Management (asynchronous)

Difficult words:
- asynchronous: runs without blocking main flow
- process: running program instance
"""

import subprocess
import time


def main() -> None:
    proc = subprocess.Popen(["python", "-c", "import time; time.sleep(2); print('Done async')"], stdout=subprocess.PIPE, text=True)
    print("Process started. PID:", proc.pid)

    while proc.poll() is None:
        print("Still running...")
        time.sleep(0.5)

    output = proc.stdout.read().strip() if proc.stdout else ""
    print("Finished with code:", proc.returncode)
    print("Output:", output)


if __name__ == "__main__":
    main()
