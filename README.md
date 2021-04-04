# Py Dividend Stock Manager

## Introduction

As stock investors, we want to buy stocks when they are cheap. As dividend stock investors, we also want to buy good dividend stocks when they are traded at discount to maximize dividend yield. However, checking stock prices every day is quite time consuming and unproductive. We can use **Py Dividend Stock Manager** to set up price alerts on the stocks we are interested in buying. It organizes a list of companies which stock prices are lower than our predetermined prices, and all we need to do is buy the stocks in the list.

Additionally, it displays current dividend yield and 10 years average dividend yield to compare stock valuation. If current dividend yield is higher than historical average dividend yield, we can think of it as a buy signal since higher current yield tells us that that stock is attractive and generates higher dividend yield.

## Demonstration (Version 3 Updated with Export to CSV Feature)

<p align="center">
  <img width="900" height="600" src="https://user-images.githubusercontent.com/41933169/113522343-b96f8700-956d-11eb-9b80-47528c0b0a47.png">
</p>

- Data can be exported to csv file automatically saved in current working directory.

## Demonstration (Version 3)

<p align="center">
  <img width="750" height="600" src="https://user-images.githubusercontent.com/41933169/113485112-05d99a80-947a-11eb-9479-89a691b8cac5.png">
</p>

- 10-Yrs Historical Average Dividend Yield feature has been added to compare with current dividend yield.
- If current dividend yield is higher than historical average dividend yield, we may assume that the stock is under-valued and it's time to buy.



## Demonstration (Version 2 Updated)
<p align="center">
  <img width="750" height="600" src="https://user-images.githubusercontent.com/41933169/113456074-42ee5000-93da-11eb-95c8-a8bb401643fa.png">
</p>

- Dividend Yield field in the list has been added.
- Unselect button has been added.
- It loads dividend data of stocks in S&P500 (previous year's annual dividend, stock symbols in S&P500)
- It only accepts symbols in S&P500 for now since it loads and uses dividend data from S&P500 only.
- We can expand the pool of stocks from just S&P500 using yfinance module. (will be implemented later)
- Name changed from pyStockPriceAlert to PyStockManager to be more general.


## Demonstration (Version 2)

<p align="center">
  <img width="700" height="600" src="https://user-images.githubusercontent.com/41933169/113353318-77470b00-930b-11eb-8ac6-a74c02284551.png">
</p>

- Graphic Interface has been updated with restructuring components on the program.
- Refresh status bar has been added.
- Automatic refresh data functionality has been added which updates price data during market hours (Mon-Fri 8am - 4pm).

## Demonstration (Version 1)

<p align="center">
  <img width="400" height="900" src="https://user-images.githubusercontent.com/41933169/113234192-cb4fe200-926e-11eb-80a2-824836db2d20.png">
</p>

- When it first runs, there is no list. When you add a symbol and its alert price, two lists will be created.
- All expensive stocks which prices are higher than our alert prices are listed on WATCHLIST. 
- All cheap stocks which prices are cheaper than our alert prices are listed on BUYLIST. These are the stocks we should consider buying.

## Installation

There are three versions of the program.

- run app.py directly on CML if you have python installed.
- run executable called app.exe inside directory 'pyStockPriceAlert_oneDir' (running time is fast as all the required files are already decompressed)
- run executable called app.exe inside directory 'pyStockPriceAlert_oneFile' (it takes some time to execute as it has to decompress all the required files)

(Executable versions are not shared on GitHub, but you can create an executable with pyinstaller!)
```
pip install pyinstaller
pyinstaller --onedir -w app.py
pyinstaller --onefile -w app.py
```

I personally prefer to use oneDir version by creating a shortcut of the executable. If you move the original app.exe out of the directory it belongs, it's not going to run!

In terms of storing data, it automatically create a database called 'stocks.db' within the same directory.

## Improvements

- ~~Currently, price data is updated based on daily prices. It would be helpful if we can retrieve real-time price data so that we can be informed during the market hours.~~
- ~~To refresh the data, we have to hit 'REFRESH LISTS' to update the price data in our database. It would be great if it automatically run refresh every fixed interval.~~
- ANY SUGGESTIONS...?


