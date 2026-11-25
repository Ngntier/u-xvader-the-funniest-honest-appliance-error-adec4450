import os

ENTRY = "ERROR E21: Unbalanced load. One sock. I have shaken for twenty minutes. It is still one sock."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if not (1 <= len(ENTRY) <= 200) or not ENTRY.strip():
        raise ValueError("entry must be 1-200 non-blank characters")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
