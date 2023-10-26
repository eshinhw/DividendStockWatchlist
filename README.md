<div align="center">

  ![coollogo_com-44991879](https://github.com/eshinhw/dividend-watchlist/assets/41933169/5fcf5b43-3377-41a4-98b1-1a5fc4a32b96)

</div>

<div align="center">

  ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/eshinhw/dividend-watchlist)
  ![GitHub issues](https://img.shields.io/github/issues/eshinhw/dividend-watchlist)
  ![GitHub pull requests](https://img.shields.io/github/issues-pr/eshinhw/dividend-watchlist)
  
</div>

<p align="center">
  <img width="900" height="600" src="https://github.com/eshinhw/dividend-watchlist/assets/41933169/19fa10a2-9f13-48e6-a265-d1e10c22f94d">
</p>

## Project Motivation

As dedicated dividend stock investors, our objective is to strategically acquire stocks at opportune moments when they are undervalued and their dividend yields are at their peak. The Dividend Watchlist serves as an investing assistant, diligently monitoring the prices of dividend-yielding stocks and promptly notifying us when they reach a favorable valuation. It meticulously curates a catalog of companies whose stock prices fall below our pre-established buy thresholds, streamlining our investment decisions.

Moreover, the app presents both the current dividend yield and the 10-year average dividend yield for comparative analysis of stock valuations. When the current dividend yield surpasses its historical average, it serves as a compelling buy signal, indicating that the stock is not only enticing but also promises a higher dividend yield.

## How to Install

There are three ways of running the program.

1. Run `app.py` directly on CML if you have python installed.

```
python app.py
```

In order to create an executable file, first install `pyinstaller`.

```
pip install pyinstaller
```

2. Run executable called `app.exe` inside directory `pyStockPriceAlert_oneDir`. The running time of this method is fast as all the required files are already decompressed.

```
pyinstaller --onedir -w app.py
```

3. Run executable called `app.exe` inside directory `pyStockPriceAlert_oneFile`. This method takes some time to execute as it has to decompress all the required files.

```
pyinstaller --onefile -w app.py
```

If you move the original `app.exe` out of the directory it belongs, it's not going to run!

For storing data, the program automatically create a database called `stocks.db` within the same directory. Stored data also can be exported in csv.
