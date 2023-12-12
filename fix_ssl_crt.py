import argparse
from pathlib import Path


def fix_file(orig_file_path: Path, dest_file_path: Path, n_skip_words: int) -> None:
    with open(orig_file_path, "rt") as f:
        words = f.read().split()
    lines = [' '.join(words[:n_skip_words])]
    lines.extend(words[n_skip_words:-n_skip_words])
    lines.append(' '.join(words[-n_skip_words:]))
    with open(dest_file_path, "wt") as f:
        f.write("\n".join(lines) + "\n")


def main(orig_key_path: Path, dest_key_path: Path, orig_crt_path: Path, dest_crt_path: Path) -> None:
    fix_file(orig_key_path, dest_key_path, n_skip_words=3)
    fix_file(orig_crt_path, dest_crt_path, n_skip_words=2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-ok", "--orig_key_path", type=Path, required=True)
    parser.add_argument("-dk", "--dest_key_path", type=Path, required=True)
    parser.add_argument("-oc", "--orig_crt_path", type=Path, required=True)
    parser.add_argument("-dc", "--dest_crt_path", type=Path, required=True)
    args = parser.parse_args()

    main(args.orig_key_path, args.dest_key_path, args.orig_crt_path, args.dest_crt_path)
