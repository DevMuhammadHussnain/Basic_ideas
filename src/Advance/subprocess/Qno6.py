"""
Qno6 - Background Process

Difficult words:
- background: runs while main program continues
- track: monitor progress/state
"""

import subprocess
import time


def main() -> None:
    proc = subprocess.Popen(["python", "-c", "import time; time.sleep(3); print('Background done')"])
    print("Background process PID:", proc.pid)

    for i in range(3):
        print(f"Main work {i+1}")
        time.sleep(1)

    code = proc.wait()
    print("Background return code:", code)


if __name__ == "__main__":
    main()
