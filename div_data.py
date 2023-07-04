import json
import pandas as pd
import yfinance as yf
import datetime as dt


def sp500_symbols():
    data = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")

    sp500 = data[0]
    sp500 = sp500[
        ["Symbol", "Security", "GICS Sector", "GICS Sub-Industry", "Date added"]
    ]

    sp500_symbols = sp500["Symbol"].values.tolist()
    sp500_sectors = list(set(sp500["GICS Sector"].values.tolist()))

    sp500_symbols_new = []

    for symbol in sp500_symbols:
        if "." in symbol:
            sp500_symbols_new.append(symbol.replace(".", "-"))
        else:
            sp500_symbols_new.append(symbol)

    return sp500_symbols_new


def retrieve_div_data_sp500():
    symbols = sp500_symbols()

    div_data = {}
    count = 0
    min_div_pay_years = 20

    for symbol in symbols:
        count += 1
        if count % 100 == 0:
            print(count)
        print(f"getting dividend data from {symbol}")
        annual_div = {}
        prices = yf.Ticker(symbol).history(period="max")
        dividends = prices[prices["Dividends"] > 0]
        if len(dividends) > 0:
            first_year = dividends.index[0].year
            last_year = dt.datetime.today().year
        else:
            continue

        # print(dividends)

        # get annual dividend sum from first year it paid out div
        for year in range(first_year, last_year):
            div_sum = dividends[dividends.index.year == year]["Dividends"].sum()
            annual_div[year] = div_sum
        # min # years
        # div_data[symbol][0] = annual dividend sum
        # div_data[symbol][1] = # years dividends were paid out

        # if len(annual_div) >= year_threshold:
        if 0 in list(annual_div.values()):
            continue
        if len(annual_div) > min_div_pay_years:
            div_data[symbol] = []
            additionals = {}
            additionals["consecutive_yrs"] = len(annual_div)
            div_data[symbol].append(annual_div)
            div_data[symbol].append(additionals)

    for symbol in div_data.keys():
        start_year = list(div_data[symbol][0].keys())[0]
        last_year = dt.datetime.today().year - 1
        prev_five_yrs = last_year - 6
        prev_fifteen_yrs = last_year - 16
        # print(f"working on {symbol} | start year = {start_year}")
        rate_change = []
        for year in range(prev_five_yrs, last_year + 1):
            rate_change.append(
                100
                * (div_data[symbol][0][year] - div_data[symbol][0][year - 1])
                / div_data[symbol][0][year - 1]
            )
        five_yrs_div_growth_avg = sum(rate_change) / len(rate_change)
        div_data[symbol][1]["5YrsDivGrowthAvg"] = five_yrs_div_growth_avg

        rate_change = []
        for year in range(prev_fifteen_yrs, last_year + 1):
            rate_change.append(
                100
                * (div_data[symbol][0][year] - div_data[symbol][0][year - 1])
                / div_data[symbol][0][year - 1]
            )
        fifteen_yrs_div_growth_avg = sum(rate_change) / len(rate_change)
        div_data[symbol][1]["15YrsDivGrowthAvg"] = fifteen_yrs_div_growth_avg

    return div_data


if __name__ == "__main__":
    with open("data/historical_div_sp500.json", "w") as fp:
        json.dump(retrieve_div_data_sp500(), fp)
