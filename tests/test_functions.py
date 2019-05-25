import pytest
import json
import pandas as pd
import pandas.util.testing as tm

from conftest import package
from conftest import load_json, load_csv

####### Preparation

# Load test_functions_parameters.json containing the scenarios for the tests
dictionary_json = load_json("test_functions_parameters.json")


####### Tests

### lowerize

arguments, values = dictionary_json["lowerize"].values()
@pytest.mark.parametrize(arguments, values)
def test_lowerize(df_filename, df_result_filename):

    df, df_result = load_csv(df_filename, "token"), load_csv(df_result_filename, "token")
    df_output = package.lowerize(df)

    tm.assert_frame_equal(df_output, df_result)


### interval

arguments, values = dictionary_json["interval"].values()
@pytest.mark.parametrize(arguments, values)
def test_interval(df_filename, low, high, df_result_filename):

    df, df_result = load_csv(df_filename, "token"), load_csv(df_result_filename, "token")
    df_output = package.interval(df, low, high)

    tm.assert_frame_equal(df_output, df_result)

### words

arguments, values = dictionary_json["words"].values()
@pytest.mark.parametrize(arguments, values)
def test_words(df_filename, df_result_filename):

    df, df_result = load_csv(df_filename, "token"), load_csv(df_result_filename, "token")
    df_output = package.words(df)

    tm.assert_frame_equal(df_output, df_result)

### punctuation

arguments, values = dictionary_json["punctuation"].values()
@pytest.mark.parametrize(arguments, values)
def test_punctuation(df_filename, df_result_filename):

    df, df_result = load_csv(df_filename, "token"), load_csv(df_result_filename, "token")
    df_output = package.punctuation(df)

    tm.assert_frame_equal(df_output, df_result)

### against

arguments, values = dictionary_json["against"].values()
@pytest.mark.parametrize(arguments, values)
def test_against(df_filename, table_filename, df_result_filename):

    df, table, df_result = load_csv(df_filename, index_col="token"), load_csv(table_filename, names=["token"]), load_csv(df_result_filename, index_col="token")
    df_output = package.against(df, table)

    tm.assert_frame_equal(df_output, df_result)
