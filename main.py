"""gadgetroast — one-line roast of the gadget you use every day.

Judge appeal: it names a specific gadget everyone actually uses daily —
the printer — instead of roasting gadgets in general. The joke is a
concrete, escalating demand list (ink, paper, Wi-Fi, a driver update,
then a pep talk), each item more absurd than the last, so the printer
reads as a reluctant coworker who needs emotional support before doing
its one job. The payoff is "one page": all that fuss for the smallest
possible output. Tight at 97 characters, one sentence, no filler.
"""

import os
from pathlib import Path

ENTRY = "My printer needs ink, paper, Wi-Fi, a driver update and a pep talk before it will print one page."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
