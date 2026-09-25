import argparse
import sys
from datetime import datetime


def parse_ts(line: str):
    try:
        return datetime.fromisoformat(line.split(" ", 1)[0])
    except ValueError:
        return None


def main(argv=None):
    p = argparse.ArgumentParser(prog="logslice")
    p.add_argument("file")
    p.add_argument("--from", dest="start", type=datetime.fromisoformat)
    p.add_argument("--to", dest="end", type=datetime.fromisoformat)
    a = p.parse_args(argv)
    with open(a.file) as f:
        for line in f:
            ts = parse_ts(line)
            if ts and (not a.start or ts >= a.start) and (not a.end or ts <= a.end):
                sys.stdout.write(line)


if __name__ == "__main__":
    main()
