#!/usr/local/bin/python3

import sys
import nltk
import re

for line in sys.stdin:
    line = line.strip()
    # Handling of paragraphs and thoughts
    regex_swann = re.compile(r"«|»|--")
    line = re.sub(regex_swann," ",line)
    # Create a list out of the sentence
    words = nltk.word_tokenize(line)
    for word in words:
        print(f"{word}===1")
