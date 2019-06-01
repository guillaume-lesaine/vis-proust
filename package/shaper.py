#!/usr/local/bin/python3

import sys
import re

for line in sys.stdin:
    line = line.replace("\n","")# if line !="\n" else line
    line = line.replace("M.","monsieur")
    line = line.replace("Mme.","madame")
    line = line.replace("Mlle.","mademoiselle")
    line = re.sub(r"«|»|\(|\)","",line)
    line = re.sub("--|—"," ",line)
    line = re.sub(r"\.|!|\?|\.\.\.","\n",line)
    if line != "":
        print(line, end=" ")
