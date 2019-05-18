#!/usr/local/bin/python3

import sys
import nltk

for line in sys.stdin:
    line = line.strip()
    # Handling of paragraphs and thoughts
    if "»--«" in line:
        line = line.replace("»--«"," ")
    if "--" in line:
        line = line.replace("--"," ")
    if "«" in line:
        line = line.replace("«","")
    if "»" in line:
        line = line.replace("»","")
    words = nltk.word_tokenize(line)
    for word in words:
        print('%s===%s' % (word, "1"))
