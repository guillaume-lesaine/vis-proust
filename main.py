# Python Librairies
import os
import pandas as pd
import re
from functools import reduce

# Custom package
import package as pkg

# Main

proust = {}
filenames = os.listdir("./output")
books = {re.split(r"-|\.",file)[0] for file in filenames}

books_order = [
    "du_cote_de_chez_swann",
    "a_l_ombre_des_jeunes_filles_en_fleurs",
    "le_cote_de_guermantes",
    "sodome_et_gomorrhe",
    "la_prisonniere",
    "albertine_disparue",
    "le_temps_retrouve"
    ]

for book in books:
    parts = [file for file in filenames if book in file]
    proust[book] = reduce(lambda x, y: x + y, [pkg.Volume(pd.read_csv("./output/" + part, delimiter="===", engine='python', names=["token", "count"]).set_index("token")) for part in parts])

# proust_recherche = pkg.Volume(reduce(lambda df1, df2: df1.add(df2, fill_value = 0), [proust[book].df for book in books]).astype(int))
# proust_lowercase = proust_recherche.get_lowercase()
# proust_titlecase = proust_recherche.get_titlecase()

# Distribution

list_titlecase = ["artists.csv", "names.csv", "cities.csv"]
list_punctuation = ["punctuation.csv"]

for file in list_titlecase:
    dataframe_source = pd.read_csv(f"./utilitaries/{file}", names=["token"])
    distribution = pd.concat([pkg.against(proust[book].get_titlecase(),dataframe_source) for book in books_order], axis=1, sort=False, ignore_index=True)
    distribution["recherche"] = distribution.sum(axis=1)
    distribution = distribution.sort_values("recherche", ascending=False)
    distribution.to_csv(f"./data/distribution_{file}", sep=",",  index_label="token")


for file in list_punctuation:
    dataframe_source = pd.read_csv(f"./utilitaries/{file}", delimiter="===", engine='python', names=["token"])
    distribution = pd.concat([pkg.against(proust[book].get_punctuation(),dataframe_source) for book in books_order], axis=1, sort=False, ignore_index=True)
    distribution["recherche"] = distribution.sum(axis=1)
    distribution = distribution.sort_values("recherche", ascending=False)
    distribution.to_csv(f"./data/distribution_{file}", sep="=",  index_label="token")



# Most common words
