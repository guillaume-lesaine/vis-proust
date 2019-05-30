import copy
import re

def lowerize(df):
    df_c = copy.deepcopy(df)
    df_c.index = df_c.index.map(lambda x : x.lower())
    df_c = df_c.groupby(df_c.index).agg({"count":"sum"})
    return df_c

def interval(df,low,high):
    if low > high:
        raise ValueError("[INPUT] low > high, should be low <= high")
    df_c = copy.deepcopy(df)
    df_c = df_c.query('count>={} & count<={}'.format(low,high))
    return df_c

def words(df):
    return df[df.index.str.contains('[A-Za-z]')]

def punctuation(df):
    punctuation_marks = ["!", ".", "?", ",", ";", "...", ":","-","--","'"]
    return df[df.index.isin(punctuation_marks)]

def against(df,table):
    table["count"] = 0
    table = table.set_index("token")
    table = (table.add(df[df.index.isin(table.index)], fill_value = 0)
                        .astype(int))
    return table

def titlecase(df):
    return df[df.index.map(lambda x: True if x[0].isupper() else False)]

def lowercase(df):
    return df[df.index.map(lambda x: True if x[0].islower() else False)]

def gem(s):
    l = re.split(r"'|-|\.|\^",s)
    if list(filter(lambda w: len(w)>=4, l)) != []:
        return True
    else :
        return False
