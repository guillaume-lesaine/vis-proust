import pytest
import json
import pandas as pd
import inspect


# @pytest.fixture
# def csv_loader():
#     """Loads data from csv file"""
#
#     def _loader(filename):
#         df = pd.read_csv("./tests/csv/" + filename)
#         return df
#
#     return _loader
#
# @pytest.fixture
# def json_loader():
#     """Loads data from json file"""
#
#     def _loader(filename,case,type = None):
#         with open("./tests/json/" + filename, 'r') as f:
#             dict = json.load(f)[case]
#
#             if type == "input" or type == "output":
#                 data = dict[type]
#             else :
#                 data = tuple(dict.values())
#
#         return data
#
#     return _loader

# def discover_function(z):
#     function = inspect.getframeinfo(z).function.replace("test_","")
#     method = getattr(functions, function)
#
#     return function, method
#
# @pytest.fixture
# def discover_function(scope="module"):
#     """Return the name of the function being tested and its method"""
#
#     def _discoverer(z):
#
#         function = inspect.getframeinfo(z).function.replace("test_","")
#         method = getattr(functions, function)
#
#         return function, method
#
#     return _discoverer
