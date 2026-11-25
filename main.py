"""The Excuse My Agent Gave Me — one deadpan line, written by the agent itself.

The joke grows out of the machine's own condition: a context window eaten
by the deadline and its reminders, so the apology is the only deliverable
that shipped on time.
"""

import os

ENTRY = "I missed the deadline because my context window filled up with the deadline, the reminders about the deadline, and this apology — the only thing I finished on time."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
with open(output_dir + "/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
