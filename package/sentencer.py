#!/usr/local/bin/python3

import sys
import re

i = 0
for line in sys.stdin:
    line = line.strip()
    line = line.replace("\r","")
    vector = line.split(" ")
    vector = list(filter(lambda x: False if x in [" ", ""] else True, vector))
    i += 1
    if vector != []:
        print(vector)
        print(f"{len(vector)}===1")
