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
    '''
        Test function of function_dataframe. This test shows an
        example of how to handle a function taking a pandas dataframe as input
        and output.

        To customize it :
            1 - Relate it to the right function by replacing the names
            2 - Give the right elements as input and parameters in "test_functions_parameters".
            3 - Add the right csv files in the /csv folder to generate your dataframe inputs and outputs.
    '''

    df, df_result = load_csv(df_filename), load_csv(df_result_filename)
    df_output = package.lowerize(df)

    tm.assert_frame_equal(df_output, df_result)


### interval

arguments, values = dictionary_json["interval"].values()
@pytest.mark.parametrize(arguments, values)
def test_interval(df_filename, low, high, df_result_filename):
    '''
        Test function of function_complex. This test shows an
        example of how to handle a complex combination of inputs and outpus.
        This test is a simple combination of the three test presented above.

        To customize it :
            1 - Relate it to the right function by replacing the names
            2 - Give the right elements as input and parameters in "test_functions_parameters".
            3 - Add the right csv files in the /csv folder to generate your dataframe inputs and outputs.
            4 - Add the right json files in the /json folder to generate your list inputs and outputs.
    '''

    df, df_result = load_csv(df_filename), load_csv(df_result_filename)
    df_output = package.interval(df, low, high)

    tm.assert_frame_equal(df_output, df_result)
