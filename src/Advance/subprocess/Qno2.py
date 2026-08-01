"""
Qno2 - Pipe Output

Difficult words:
- capture: save output for later use
- pipe: pass output of one command as input/usable data
"""

import subprocess


def main() -> None:
    result = subprocess.run(["python", "-c", "print('python beginners')"], capture_output=True, text=True)
    output_text = result.stdout.strip()
    print("Captured output:", output_text)
    print("Upper case:", output_text.upper())


if __name__ == "__main__":
    main()
