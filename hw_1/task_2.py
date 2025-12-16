#! /usr/bin/env python3

import sys


def main():
    if len(sys.argv) > 1:
        filenames = sys.argv[1:]
        for i, filename in enumerate(filenames):
            if len(filenames) > 1:
                if i > 0:
                    print()
                print(f"==> {filename} <==")
            with open(filename, 'r') as f:
                lines = f.readlines()
            for line in lines[-10:]:
                print(line, end='')
    else:
        lines = sys.stdin.readlines()
        for line in lines[-17:]:
            print(line, end='')


if __name__ == "__main__":
    main()
