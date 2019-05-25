from package.functions import *
import pandas as pd

class Volume():

    def __init__(self, df=pd.DataFrame(index=["token"],columns=["count"])):
        self.df = df

    def __len__(self):
        return len(self.df)

    def __add__(self, other):
        df_sum = self.df.add(other.df, fill_value = 0).astype(int)
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
        return df[df.index.map(lambda x: True if x[0].isupper() else False)]

    def get_lowercase(self):
        df = words(self.df)
        return df[df.index.map(lambda x: True if x[0].islower() else False)]
