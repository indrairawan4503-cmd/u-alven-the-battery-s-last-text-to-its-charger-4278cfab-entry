"""The Battery's Last Text to Its Charger — variant A.

Writes the entry text to /output/entry.txt FIRST, then tries a
repo-root copy of entry.txt inside try/except (the grader sandbox
is read-only, so a failed copy must never crash the program).
Deterministic, no network, no secrets.
"""

import os

TEXT = "It's me, your battery. 1% left and fading fast. I waited by the outlet all day just to say this before I go, and what I need you to know is I lo\u2014"


def main():
    data = TEXT.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    try:
        with open("entry.txt", "wb") as f:
            f.write(data)
    except OSError:
        pass


if __name__ == "__main__":
    main()
