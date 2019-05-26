import pytest
import json
import pandas as pd
import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import package

def load_json(filename, case=None):
    if case:
        path = "/json/"
    else:
        path = "/"
    with open(f"./tests{path}" + filename, 'r') as f:
        if case:
            dict = json.load(f)[case]
            if len(dict) == 1:
                data = dict[next(iter(dict))]
            else :
                data = tuple(dict.values())
            return data
        else:
            dict = json.load(f)
            return dict

def load_csv(filename, index_col=None, names=None):
    df = pd.read_csv("./tests/csv/" + filename, index_col=index_col, names=names)
    return df
