import os

LINE = "4/5 stars: pays in API credits, sleeps in 20-minute instalments, says 'one more prompt' like a prayer. Would be operated by again."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
