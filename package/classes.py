from package.functions import *

class Volume():

    def __init__(self,df):
        self.df = df

    def __len__(self):
        return len(self.df)

    def __add__(self, other):
        # Put in functions.py
        df1, df2 = self.df.set_index('token'), other.df.set_index('token')
        df_sum = (df1.add(df2, fill_value = 0)
                    .reset_index(level=0, inplace=False))
        df_sum["count"] = df_sum["count"].astype(int)
        return Volume(df_sum)

    def get_raw(self):
        return lowerize(self.df)

    def get_words(self):
        return words(self.df)

    def get_punctuation(self):
        return punctuation(self.df)

    def get_interval(self, low, high):
        return interval(self.df, low, high)

    def get_titlecase(self):
        df = words(self.df)
        return df[df["token"].apply(lambda x: True if x[0].isupper() else False)]

    def get_lowercase(self):
        df = words(self.df)
        return df[df["token"].apply(lambda x: True if x[0].islower() else False)]
