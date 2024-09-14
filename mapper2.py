#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    # print(f"{words[4]} {words[1]} {words[0]} {words[2]} {words[3]} {words[5]} {words[6]}")
    # print(line)
    print(f"{words[1]} {words[2]} {words[0]} {words[4]} {words[3]} {words[5]} {words[6]}")
