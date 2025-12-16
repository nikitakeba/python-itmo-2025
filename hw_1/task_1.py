#! /usr/bin/env python3
import sys


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        with open(filename, 'r') as f:
            lines = f.readlines()
    else:
        lines = sys.stdin.readlines()

    for i, line in enumerate(lines, start=1):
        print(f"{i:6}\t{line}", end='')


if __name__ == "__main__":
    main()
