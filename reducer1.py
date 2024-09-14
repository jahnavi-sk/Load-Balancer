#!/usr/bin/env python3

import sys

# old_line = None
# predicted=[]
# lines=[]

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    # print(len(words))
    # print(len(words))
    if len(words)==2:
        # print("hi")
        predicted = words[1]
    elif len(words)>2:
        # print(len(words))
        # print(line,predicted)
        if len(words)==5:
            
            print(f"{words[2]} {words[3]} {words[0]} 0.0 {words[1]} {words[4]} {predicted}")

            # print(f"{words[1]} {words[3]} {words[0]} 0.0 {words[2]} {words[4]} {predicted}")

            # print(f"{words[2]} {words[3]} 0.0 {words[0]} {words[1]} {words[4]} {predicted}")
        elif len(words)==6:
           
            print(f"{words[2]} {words[3]} {words[0]} {words[4]} {words[1]} {words[5]} {predicted}")

            # print(f"{words[1]} {words[3]} {words[0]} {words[4]} {words[2]} {words[5]} {predicted}")

            # print(f"{words[2]} {words[3]} {words[4]} {words[0]} {words[1]} {words[5]} {predicted}")

            
        # print(f"{words[2]}")
# sorted_lines = sorted(lines, key=lambda x: (x[0], x[1], x[2]))

# for _, _,_, formatted_line in sorted_lines:
#     print(formatted_line)