# Python Librairies
import os
import pandas as pd
import re
from functools import reduce
import sys
import argparse

# Custom package
import package as pkg

# Variables

parser = argparse.ArgumentParser(description='Variables')
parser.add_argument('--case')

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

for book in books:
    parts = [file for file in filenames if book in file]
    proust[book] = reduce(lambda acc, df: acc.add(df, fill_value = 0),
        [pd.read_csv(f"./outputs/{args.case}/" + part, delimiter="===", engine='python', names=["variable", "count"]).set_index("variable") for part in parts]
    )

proust_recherche = reduce(lambda acc, df: acc.add(df, fill_value = 0), [proust[book] for book in books])

# Distribution

distrib_func = pd.read_csv(f"./utilitaries/distribution_functions.csv", index_col="file")
distrib_func = distrib_func[distrib_func.index.map(lambda x: True if args.case in x else False)]

for file in distrib_func.index:
    dataframe_source = pd.read_csv(f"./utilitaries/{file}", sep="=", names=["variable"])
    distribution = pd.concat([pkg.against(getattr(pkg, distrib_func.loc[file, "function"])(proust[book]),dataframe_source) for book in books], axis=1, sort=False, ignore_index=True)
    #distribution["recherche"] = distribution.sum(axis=1)
    # distribution = distribution.sort_values("recherche", ascending=False)
    distribution.to_csv(f"./data/distribution_{file}", sep="=",  index_label="expression")

# Frequence

dataframe_values = pd.read_csv(f"./utilitaries/frequence_values.csv", index_col="case")
value = dataframe_values.loc[args.case, "value"]

valuable_ngrams = pkg.lowerize(proust_recherche).query(f"count >= {value}")
frequent = pd.concat([pkg.against(pkg.lowerize(proust[book]), valuable_ngrams) for book in books], axis=1, sort=False, ignore_index=True)
frequent.to_csv(f"./data/frequence_{args.case}.csv", sep=",",  index_label="expression")

# Histogram des 2grams, 3grams, 4grams, 5grams, 6grams

# proust_words_lowerize = pkg.words(pkg.lowerize(proust_recherche))
# proust_gems = proust_words_lowerize[proust_words_lowerize.index.map(lambda x: pkg.gem(x))]
#
# print(pkg.interval(proust_gems,5000,20000))
