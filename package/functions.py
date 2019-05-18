import pandas as pd
import copy

def lowerize(df):
    df_c = copy.deepcopy(df)
    df_c["token"] = df_c["token"].apply(lambda x : x.lower())
    df_c = (df_c.groupby(["token"]).sum().reset_index(level=0, inplace=False)
            .sort_values("token"))
    return df_c

def interval(df,low,high):
    if low > high:
        raise ValueError("[INPUT] low > high, should be low <= high")
    df_c = copy.deepcopy(df)
    df_c = (df_c.query('count>={} & count<={}'.format(low,high))
            .reset_index(level=0, inplace=False)
            .drop("index", axis=1))
    return df_c

def words(df):
    df = df[df["token"].str.contains('[A-Za-z]')]
    return df

def punctuation(df):
    punctuation_marks = ["!", ".", "?", ",", ";", "...", ":"]
    df = (df[df["token"].isin(punctuation_marks)]
            .reset_index(level=0, inplace=False)
            .drop("index", axis=1))
    return df
