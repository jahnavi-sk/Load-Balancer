#!/usr/bin/env python3

import sys

endpoint_scores = {
    'user/profile': 100,
    'user/settings': 200,
    'order/history': 300,
    'order/checkout': 400,
    'product/details': 500,
    'product/search': 600,
    'cart/add': 700,
    'cart/remove': 800,
    'payment/submit': 900,
    'support/ticket': 1000
}

for line in sys.stdin:
    line = line.strip()
    if len(line)>1:
        words = line.split()
        if len(words)>2:
            cost = endpoint_scores.get(words[2])
            print(line,cost)
            # print(f"{words[2]} {words[3]}")
        else:
            print(line)

