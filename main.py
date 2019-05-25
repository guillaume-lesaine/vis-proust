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

for book in books:
    parts = [file for file in filenames if book in file]
    proust[book] = reduce(lambda x, y: x + y, [pkg.Volume(pd.read_csv("./output/" + part, delimiter="===", engine='python', names=["token", "count"]).set_index("token")) for part in parts])

proust_lowercase = reduce(lambda df1, df2: df1.add(df2, fill_value = 0), [proust[book].get_lowercase() for book in books]).astype(int)
proust_titlecase = reduce(lambda df1, df2: df1.add(df2, fill_value = 0), [proust[book].get_titlecase() for book in books]).astype(int)

# Presence

dataframe_names = pd.read_csv("./utilitaries/names.csv", names=["token"])
dataframe_cities = pd.read_csv("./utilitaries/cities.csv", names=["token"])
dataframe_names["count"], dataframe_cities["count"] = 0, 0
dataframe_names, dataframe_cities = dataframe_names.set_index("token"), dataframe_cities.set_index("token")

dataframe_names = (dataframe_names.add(proust_titlecase[proust_titlecase.index.isin(dataframe_names.index)], fill_value = 0)
                    .astype(int)
                    .sort_values("count", ascending=False))

dataframe_cities = (dataframe_cities.add(proust_titlecase[proust_titlecase.index.isin(dataframe_cities.index)], fill_value = 0)
                    .astype(int)
                    .sort_values("count", ascending=False))
print(dataframe_names)
print(dataframe_cities)
