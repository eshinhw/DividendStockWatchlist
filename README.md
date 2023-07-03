# Dividend Watchlist

<p align="center">
  <img width="900" height="600" src="https://github.com/eshinhw/dividend-watchlist/assets/41933169/19fa10a2-9f13-48e6-a265-d1e10c22f94d">
</p>

## Introduction

As dividend stock investors, we want to buy stocks when they are under-valued and their dividend yields are high. Dividend Watchlist helps keeping track of prices of dividend stocks and providing price alerts when they are under-valued. It organizes a list of companies which stock prices are lower than our predetermined prices in a buy list, and all we need to do is buy the stocks in the list.

Additionally, it displays current dividend yield and 10 years average dividend yield to compare stock valuation. If current dividend yield is higher than historical average dividend yield, we can think of it as a buy signal since higher current yield tells us that that stock is attractive and generates higher dividend yield.

## Installation

There are three versions of the program.

1. Run `app.py` directly on CML if you have python installed.
2. Run executable called app.exe inside directory 'pyStockPriceAlert_oneDir' (running time is fast as all the required files are already decompressed)
3. Run executable called app.exe inside directory 'pyStockPriceAlert_oneFile' (it takes some time to execute as it has to decompress all the required files)

Executable versions are not shared on GitHub, but you can create an executable with pyinstaller by running the following commands.

```
pip install pyinstaller
pyinstaller --onedir -w app.py
pyinstaller --onefile -w app.py
```

I prefer to use `--onedir` by creating a shortcut of the executable. If you move the original `app.exe` out of the directory it belongs, it's not going to run!

In terms of storing data, it automatically create a database called `stocks.db` within the same directory. Stored data also can be exported in csv.
