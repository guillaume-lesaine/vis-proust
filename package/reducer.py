#!/usr/local/bin/python3

import sys

# wordcount = {}

current_word = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
    try:
        word, count = line.split("===")
    except:
        continue

    try :
        count = int(count)
    except :
        continue

    # This part only works because of the sort in the command line
    if current_word == word:
        current_count += count
    else :
        if current_word:
            print("{}==={}".format(current_word,current_count))
        current_count = count
        current_word = word

if current_word == word :
    print("{}==={}".format(current_word,current_count))
