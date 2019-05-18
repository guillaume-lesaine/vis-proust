from package import functions
import pandas as pd

dataframe = pd.read_csv("output_count.csv", delimiter="===", engine='python')
dataframe.columns = ["token","count"]

dataframe_words = dataframe.query('count>10')
# dataframe_words["token"] = dataframe_words.loc[dataframe_words.loc[:,"token"] ==].apply(lambda x : )

print(dataframe["count"].sum())
print(dataframe[dataframe["token"].str.contains('[^A-Za-z]')]["count"].sum())
