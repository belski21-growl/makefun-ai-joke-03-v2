"""ai-joke-03 v2: one joke about an AI coding agent.
Writes the joke to entry.txt with no trailing newline.
"""

import os

JOKE = "My coding agent fixed the memory leak by restarting the server every hour. Uptime is now 59 minutes. The dashboard calls it 'self-healing.'"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(JOKE)  # exact bytes, no trailing newline


if __name__ == "__main__":
    main()
