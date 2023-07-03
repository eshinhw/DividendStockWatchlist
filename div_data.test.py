import unittest
from div_data import sp500_symbols
from div_data import retrieve_div_data_sp500

class TestSymbols(unittest.TestCase):
    pass

if __name__ == "__main__":
    # print(sp500_symbols())
    print(retrieve_div_data_sp500())