import unittest
import app


class TestAdd(unittest.TestCase):
    pass


if __name__ == "__main__":
    # print(_get_close_and_historical_div_yield('MMM'))
    # print(app.get_current_price("MMM"))
    print(app.get_historical_dividend_yield("ABT"))
