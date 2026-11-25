# SPDX-License-Identifier: MIT
"""Tell a Whole Story in 32 Characters -- make.fun entry.

Writes a single Wi-Fi network name (at most 32 characters) to
/output/entry.txt. The name is a fixed, hand-written string: the program
is fully deterministic, uses only the standard library, and touches no
network.

The name: a couple whose therapy failed, so instead of fixing the
marriage they bought mesh Wi-Fi. Beginning (therapy), middle (it
failed), end (a mesh router now papers over the silence). The joke
lands on the first read; the story is the whole arc in 28 characters.
"""

import os

ENTRY = "TherapyFailed_BoughtMeshWiFi"


def main() -> None:
    if not 1 <= len(ENTRY) <= 32:
        raise ValueError(f"entry must be 1-32 characters, got {len(ENTRY)}")
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the gate counts the file's characters, so the
    # file must hold exactly the 28-character name, nothing more.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"{ENTRY} ({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
