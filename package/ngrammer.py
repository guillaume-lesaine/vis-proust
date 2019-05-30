#!/usr/local/bin/python3

import sys
import nltk
import re

for line in sys.stdin:
    line = line.strip()
    line = line.replace("\n","")
    line = re.split(r",|;|:", line)
    line = tuple(filter(None,line))
    for part in line:
        grams = nltk.ngrams(part.split(), int(sys.argv[1]))
        for gram in grams:
            gram = " ".join(gram)
            print(f"{gram}===1")
