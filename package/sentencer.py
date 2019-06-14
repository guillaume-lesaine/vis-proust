#!/usr/local/bin/python3

import sys
import re

for line in sys.stdin:
    line = line.lstrip()
    line = re.sub(r"\r", "", line)
    print(line, end="")
