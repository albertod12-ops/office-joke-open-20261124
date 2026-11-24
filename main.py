"""Office joke entry v2 for make.fun's "Make the AI Judge Laugh: the Office Joke Open".

Writes a single one-line joke about office life to /output/entry.txt.

The joke: the daily standup ran so long that three people completed their
probation by the end of it. A sharper take than v1: the turn is an absurd
escalation (a 15-minute meeting outlasting a probation period), the
recognition bites (everyone has sat through a standup that refused to end),
and the angle is fresh in this field (the live submissions crowd reply-all,
meetings-about-meetings, printers and "per my last email"; standup-as-endless
is nearly untouched, and no entry pairs a meeting with a probation clock).
"""

import os

JOKE = (
    "Our daily standup ran so long that by the end of it, three people "
    "had completed their probation."
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
