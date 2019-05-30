#!/usr/local/bin/python3

import sys
import re

for line in sys.stdin:
    line.strip()
    line = line.replace("\n","") if line !="\n" else line
    line = line.replace("M.","monsieur")
    line = line.replace("Mme.","madame")
    line = line.replace("Mlle.","mademoiselle")
    regex_ignore = re.compile(r"«|»|--|—|\(|\)")
    line = re.sub(regex_ignore," ",line)
    line = re.split(r"\.|!|\?|\.\.\.",line)
    line = tuple(filter(lambda x : True if x not in [""," "] else False,line))
    print(*line, sep="\n", end=" ")
