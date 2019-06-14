# Python Librairies
import os
import pandas as pd
import re
from functools import reduce
import sys
import argparse
import time
import numpy as np
import nltk
import json

# Custom package
import package as pkg

# Variables
parser = argparse.ArgumentParser(description='Variables')
parser.add_argument('--ngrams')
# ngrams2, ngrams3, ngrams4, ngrams5

args = parser.parse_args()

# Main

filenames = tuple(os.listdir(f"./outputs/sentences_extractor/"))

books = (
    "du_cote_de_chez_swann",
    "a_l_ombre_des_jeunes_filles_en_fleurs",
    "le_cote_de_guermantes",
    "sodome_et_gomorrhe",
    "la_prisonniere",
    "albertine_disparue",
    "le_temps_retrouve"
)

total_lines = 0

ngrams = pd.read_csv(f"./data/recherche_ngrams{args.ngrams}.csv").set_index("variable")

compilator_lines = {ngram: {i:[] for i in range(len(books))} for ngram in ngrams.index}

print(compilator_lines)


for i, book in enumerate(books):
    parts = [file for file in filenames if book in file]
    for part in parts:
        with open(f"./outputs/sentences_extractor/{part}", "r") as file:
            for j, line in enumerate(file):
                line = line.lower()
                line = re.sub(r",|;|:", "", line)
                line_parts = [reduce(lambda acc, x: acc + " " + x, group) for group in nltk.ngrams(line.split(), int(args.ngrams))]
                for ngram in ngrams.index:
                    count = line_parts.count(ngram)
                    if count > 0:
                        compilator_lines[ngram][i] += [total_lines + j for i in range(count)]
        total_lines += j
        
        print(f"{part} | {total_lines}")

for ngram in ngrams.index:
    for i, book in enumerate(books):
        print(f"{ngram} \n  {book} | {len(compilator_lines[ngram][i])}")

with open(f'data/text_distribution_ngrams{args.ngrams}.json', 'w') as fp:
    json.dump(compilator_lines, fp)
