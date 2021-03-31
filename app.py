import os
import sqlite3
import tkinter as tk
import datetime as dt
import pandas_datareader.data as web

# from tkinter import ttk
# from tkinter import filedialog, Text

def _get_close_price(symbol):
    startDate = (dt.date.today() - dt.timedelta(days=1)).strftime("%Y-%m-%d")
    endDate = dt.date.today().strftime("%Y-%m-%d")
    close = web.DataReader(symbol, 'yahoo', startDate, endDate)['Adj Close'].iloc[-1].round(2)
    return close

def _clear_input():
    symbol_input.delete(0, tk.END)
    price_input.delete(0, tk.END)

def add():
    conn = sqlite3.connect('price_alert.db')
    c = conn.cursor()

    # Create a table
    c.execute("""CREATE TABLE IF NOT EXISTS prices (
        symbol text,
        target_price real,
        current_price real
        ) """
              )
    # INPUT VALIDITY CHECK
    s = symbol_input.get()
    tp = price_input.get()
    if (s == "") or (not str(tp).isnumeric()) or (tp <= 0):
        _clear_input()
        return
    try:
        cp = _get_close_price(s)
    except:
        _clear_input()
        return

    # Insert into table
    c.execute("INSERT INTO prices VALUES (:symbol, :target_price, :current_price)",
              {
                  'symbol': s.upper(),
                  'target_price': tp,
                  'current_price': cp
              })

    _clear_input()
    conn.commit()
    conn.close()

def delete():
    conn = sqlite3.connect('price_alert.db')
    c = conn.cursor()

    #c.execute("DELETE from prices_v2 WHERE symbol=")

    conn.commit()
    conn.close()

def query():
    conn = sqlite3.connect('price_alert.db')
    c = conn.cursor()

    c.execute("SELECT *, oid FROM prices")
    records = c.fetchall() # fetches all records
    output_records = ""
    for record in records:
        print(record)
        output_records += str(record[3]) + '\t' + str(record[0]) + '\t' + str(record[1]) + '\t' + str(record[2]) + '\n'

    outputLabel = tk.Label(root, text=output_records)
    outputLabel.grid(row=8, column=0)

    conn.close()

root = tk.Tk()
root.title("Stock Price Alert")
root.geometry("400x400")

symbol = tk.Label(root, text="Symbol", width=30)
symbol.grid(row=0,column=0)
symbol_input = tk.Entry()
symbol_input.grid(row=1, column=0)
target_price = tk.Label(root, text="Target Price", width=30)
target_price.grid(row=2,column=0)
price_input = tk.Entry()
price_input.grid(row=3,column=0)
addButton = tk.Button(root, text="ADD", command=add, width=30)
addButton.grid(row=4,column=0, pady=10)
query_btn = tk.Button(root, text="QUERY", command=query, width=30)
query_btn.grid(row=5, column=0, pady=10)
del_btn = tk.Button(root, text="DELETE", command=delete, width=30)
del_btn.grid(row=6, column=0, pady=10)
# query_header = tk.Label(root, text="Symbol" + '\t' +"Target Price")
# query_header.grid(row=7, column=0)


# tree = ttk.Treeview(root, column=("c1", "c2"), show='headings')
# tree.column("#1", anchor=tk.CENTER)

# tree.heading("#1", text="SYMBOL")

# tree.column("#2", anchor=tk.CENTER)

# tree.heading("#2", text="TARGET")

# tree.grid(row=2, column=0, columnspan=6)



root.mainloop()