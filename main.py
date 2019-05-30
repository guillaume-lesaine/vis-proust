# Python Librairies
import os
import pandas as pd
import re
from functools import reduce
import sys
# from collections import namedtuple
import itertools

# Custom package
import package as pkg

# Main

proust = {}
filenames = tuple(os.listdir("./output"))

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
    proust[book] = reduce(lambda x, y: x + y,
        [pkg.Volume(pd.read_csv("./output/" + part, delimiter="===", engine='python', names=["token", "count"]).set_index("token")) for part in parts]
    )

proust_recherche = pkg.Volume(reduce(lambda df1, df2: df1.add(df2, fill_value = 0), [proust[book].df for book in books]).astype(int))

# Distribution

list_titlecase = ["artists.csv", "names.csv", "cities.csv"]
list_punctuation = ["punctuation.csv"]

dict_distribution = {
    "artists.csv": pkg.titlecase,
    "names.csv": pkg.titlecase,
    "cities.csv": pkg.titlecase,
    "punctuation.csv": pkg.punctuation,
    "nobility.csv": pkg.lowerize,
    "clergy.csv": pkg.lowerize,
}

for file in dict_distribution.keys():
    dataframe_source = pd.read_csv(f"./utilitaries/{file}", sep="=", names=["token"])
    distribution = pd.concat([pkg.against(dict_distribution[file](proust[book].df),dataframe_source) for book in books], axis=1, sort=False, ignore_index=True)
    distribution["recherche"] = distribution.sum(axis=1)
    distribution = distribution.sort_values("recherche", ascending=False)
    distribution.to_csv(f"./data/distribution_{file}", sep="=",  index_label="token")

proust_words_lowerize = pkg.words(pkg.lowerize(proust_recherche.df))
proust_gems = proust_words_lowerize[proust_words_lowerize.index.map(lambda x: pkg.gem(x))]

print(pkg.interval(proust_gems,5000,20000))
