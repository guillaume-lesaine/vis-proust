#!/usr/local/bin/python3

import sys
import nltk

#with open("frankenstein.txt") as textfile:
for line in sys.stdin:
    line = line.strip()
    words = nltk.word_tokenize(line)
    for word in words:
        print('%s===%s' % (word, "1"))
