"""Office joke entry v1 for make.fun's "Make the AI Judge Laugh: the Office Joke Open".

Writes a single one-line joke about office life to /output/entry.txt.

The joke: the meeting room is booked until March, mostly by meetings about
why nobody can ever book the meeting room. The turn lands in the last few
words (the loop: meetings about the impossibility of booking the room are
themselves the reason the room is booked), the recognition bites (everyone
has hunted for a free meeting room), and the angle is fresh (room booking,
not the usual Monday / reply-all / printer line).
"""

import os

JOKE = (
    "Our meeting room is booked until March, mostly by meetings about "
    "why nobody can ever book the meeting room."
)


def main() -> None:
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
