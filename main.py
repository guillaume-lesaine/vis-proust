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
    proust[book] = reduce(lambda x, y: x + y, [pkg.Volume(pd.read_csv("./output/" + part, delimiter="===", engine='python', names=["token","count"])) for part in parts])
    print(proust[book].get_raw())
