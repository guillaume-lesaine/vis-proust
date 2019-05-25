import copy

def lowerize(df):
    df_c = copy.deepcopy(df)
    df_c.index = df_c.index.map(lambda x : x.lower())
    df_c = df_c.groupby(df_c.index).sum()
    return df_c

def words(df):
    return df[df.index.str.contains('[A-Za-z]')]

def punctuation(df):
    punctuation_marks = ["!", ".", "?", ",", ";", "...", ":"]
    return df[df.index.isin(punctuation_marks)]

def interval(df,low,high):
    if low > high:
        raise ValueError("[INPUT] low > high, should be low <= high")
    df_c = copy.deepcopy(df)
    df_c = df_c.query('count>={} & count<={}'.format(low,high))
    return df_c
