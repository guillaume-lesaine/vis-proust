from package import functions
import os
import pandas as pd

filenames = os.listdir("./output")

dataframe = pd.read_csv("./output/" + "du_cote_de_chez_swann.csv", delimiter="===", engine='python')
dataframe.columns = ["token","count"]

dataframe_lowerize = functions.lowerize(dataframe)
dataframe_interval = functions.interval(dataframe, 200, 300)
dataframe_words = functions.words(dataframe)
dataframe_punctuation = functions.punctuation(dataframe)
dataframe_capitalized = dataframe_words[dataframe_words["token"].apply(lambda x: True if x[0].isupper() else False)]

print(dataframe_lowerize)
print(dataframe_interval)
print(dataframe_words)
print(dataframe_punctuation)
print(dataframe_capitalized)
