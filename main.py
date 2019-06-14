# Python Librairies
import os
import pandas as pd
import re
from functools import reduce
import sys
import argparse
import time
import numpy as np

# Custom package
import package as pkg

# Variables

parser = argparse.ArgumentParser(description='Variables')
parser.add_argument('--case')
# tokens, sentences, ngrams2, ngrams3, ngrams4

args = parser.parse_args()

# Main

proust = {}
filenames = tuple(os.listdir(f"./outputs/{args.case}"))

books = (
    "du_cote_de_chez_swann",
    "a_l_ombre_des_jeunes_filles_en_fleurs",
    "le_cote_de_guermantes",
    "sodome_et_gomorrhe",
    "la_prisonniere",
    "albertine_disparue",
    "le_temps_retrouve"
)

for i, book in enumerate(books):
    parts = [file for file in filenames if book in file]
    proust[book] = reduce(lambda acc, df: acc.add(df, fill_value = 0),
        [pd.read_csv(f"./outputs/{args.case}/" + part, delimiter="===", engine='python', names=["variable", "count"]).set_index("variable") for part in parts]
    )

proust_recherche = reduce(lambda acc, df: acc.add(df, fill_value = 0), [proust[book] for book in books]).astype(int)
proust_recherche.to_csv(f"./data/recherche_{args.case}.csv", sep=",",  index_label="variable")

# Macro Analysis

if args.case == "sentences":
    sentences_comparison = pd.concat([proust[book] for book in books], axis=1, sort=False, ignore_index=True).fillna(0).astype(int)
    sentences_comparison.to_csv(f"./data/sentences.csv", sep=",",  index_label="variable")
    print(sentences_comparison)

# N-grams Analysis

elif "ngrams" in args.case:

    dataframe_values = pd.read_csv(f"./utilitaries/frequence_values.csv", index_col="case")
    value = dataframe_values.loc[args.case, "value"]

    valuable_ngrams = pkg.lowerize(proust_recherche).query(f"count >= {value}")

    proust_words_lowerize = pkg.words(valuable_ngrams)
    proust_gems = proust_words_lowerize[proust_words_lowerize.index.map(lambda x: pkg.gem(x))]
    proust_gems = proust_gems.sort_values("count", ascending = False)
    proust_gems.to_csv(f"./data/recherche_{args.case}.csv", sep=",")

# Thematic Analysis

else:

    distrib_func = pd.read_csv(f"./utilitaries/distribution_functions.csv", index_col="file")
    distrib_func = distrib_func[distrib_func.index.map(lambda x: True if args.case in x else False)]

    for file in distrib_func.index:
        dataframe_source = pd.read_csv(f"./utilitaries/{file}", sep="=", names=["variable"])

        distribution = pd.concat([pkg.against(getattr(pkg, distrib_func.loc[file, "function"])(proust[book]), dataframe_source) for book in books], axis=1, sort=False, ignore_index=True).astype(int)
        distribution.to_csv(f"./data/distribution_{file}", sep=",",  index_label="expression")

        distribution_recherche = pkg.against(getattr(pkg, distrib_func.loc[file, "function"])(proust_recherche), dataframe_source).astype(int)
        distribution_recherche.to_csv(f"./data/recherche_{file}", sep=",",  index_label="expression")
