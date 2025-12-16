#! /usr/bin/env python3

import sys


def count_stats(content):
    lines = content.count('\n')
    words = len(content.split())
    bytes_count = len(content.encode('utf-8'))
    return lines, words, bytes_count

def main():
    if len(sys.argv) > 1:
        filenames = sys.argv[1:]
        total_lines = 0
        total_words = 0
        total_bytes = 0

        for filename in filenames:
            with open(filename, 'r') as f:
                content = f.read()
            lines, words, bytes_count = count_stats(content)
            total_lines += lines
            total_words += words
            total_bytes += bytes_count
            print(f"{lines:8}{words:8}{bytes_count:8} {filename}")

        if len(filenames) > 1:
            print(f"{total_lines:8}{total_words:8}{total_bytes:8} total")
    else:
        content = sys.stdin.read()
        lines, words, bytes_count = count_stats(content)
        print(f"{lines:8}{words:8}{bytes_count:8}")


if __name__ == "__main__":
    main()
