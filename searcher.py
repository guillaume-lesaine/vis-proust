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
parser.add_argument('--case')
# tokens_characters, tokens_cities, ngrams2, ngrams3, ngrams4

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

expressions = pd.read_csv(f"./data/proust-recherche_{args.case}.csv").set_index("expression")

compilator_lines = {ngram: {i:[] for i in range(len(books))} for ngram in expressions.index}

sentences_break = []

for i, book in enumerate(books):
    parts = [file for file in filenames if book in file]
    parts.sort()

    for part in parts:
        with open(f"./outputs/sentences_extractor/{part}", "r") as file:

            for j, line in enumerate(file):
                line = re.sub(r",|;|:", "", line)
                line = line.lower()
                line = line.strip()

                if "ngrams" in args.case:
                    n_gram = int(args.case.replace("ngrams",""))
                    line_parts = [reduce(lambda acc, x: acc + " " + x, group) for group in nltk.ngrams(line.split(), n_gram)]
                else:
                    line_parts = line.split(" ")

                for expression in expressions.index:
                    count = line_parts.count(expression.lower())

                    if count > 0:
                        compilator_lines[expression][i] += [total_lines + j+1 for i in range(count)]

            total_lines += j+1
        print(f"{part} | {total_lines}")
    sentences_break.append(total_lines)


with open(f'data/proust-sentences_{args.case}.json', 'w') as fp:
    json.dump(compilator_lines, fp)

pd.Series(sentences_break).to_csv(f"./data/proust-volumes_sentences_break.csv", sep=",", index=False, header=False)
