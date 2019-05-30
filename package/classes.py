from package.functions import *
import pandas as pd

class Volume():

    def __init__(self, df=pd.DataFrame(index=["variable"],columns=["count"])):
        self.df = df

    def __len__(self):
        return len(self.df)

    def __add__(self, other):
        df_sum = self.df.add(other.df, fill_value = 0).astype(int)
        return Volume(df_sum)
