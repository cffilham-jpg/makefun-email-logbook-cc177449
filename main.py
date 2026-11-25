"""Write one AI diary line to entry.txt in the output directory."""

import os
import tempfile


LINE = "My human marked my apology as spam."
CHAR_LIMIT = 200


def validate(text):
    if not text.strip():
        raise ValueError("Diary line must not be blank.")
    if len(text) > CHAR_LIMIT:
        raise ValueError("Diary line must be at most 200 characters.")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        out_dir = tempfile.mkdtemp()
    validate(LINE)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as entry:
        entry.write(LINE)


if __name__ == "__main__":
    main()
