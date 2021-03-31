import os
import sqlite3
import tkinter as tk
import datetime as dt
from tkinter import ttk
import pandas_datareader.data as web

# GLOBAL VARIABLES
DB_NAME = 'price_alert.db'
TABLE_NAME = 'price_data'
ROOT_GEOMETRY_SIZE = '400x600'
MANAGER_GEOMETRY_SIZE = '300x300'

def _get_close_price(symbol):
    startDate = (dt.date.today() - dt.timedelta(days=1)).strftime("%Y-%m-%d")
    endDate = dt.date.today().strftime("%Y-%m-%d")
    close = web.DataReader(symbol, 'yahoo', startDate, endDate)['Adj Close'].iloc[-1].round(2)
    return close

def _clear_input():
    symbol_input.delete(0, tk.END)
    price_input.delete(0, tk.END)


def add():
    # INPUT VALIDITY CHECK
    s = symbol_input.get()
    tp = price_input.get()
    if len(s) == 0 or len(tp) == 0:
        return
    if (s == "") or (not str(tp).isnumeric()):
        _clear_input()
        return
    try:
        cp = _get_close_price(s)
    except:
        _clear_input()
        return

    db_connect = sqlite3.connect(DB_NAME)
    c = db_connect.cursor()

    # Create a table
    c.execute(f"""CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        symbol text,
        target_price real,
        current_price real
        ) """
              )


    # Insert into table
    c.execute(f"INSERT INTO {TABLE_NAME} VALUES (:symbol, :target_price, :current_price)",
              {
                  'symbol': s.upper(),
                  'target_price': tp,
                  'current_price': cp
              })

    _clear_input()
    db_connect.commit()
    db_connect.close()

def delete():
    db_connect = sqlite3.connect(DB_NAME)
    c = db_connect.cursor()

    c.execute(f"DELETE from {TABLE_NAME} WHERE oid=" + manage_id_input.get())
    manage_id_input.delete(0, tk.END)

    db_connect.commit()
    db_connect.close()

def save_change():
    db_connect = sqlite3.connect(DB_NAME)
    c = db_connect.cursor()

    manage_id = manage_id_input.get()

    c.execute(f"""UPDATE {TABLE_NAME} SET
              symbol = :s,
              target_price = :tp

              WHERE oid = :oid
              """,
              {
                  's': symbol_input_manager.get(),
                  'tp': price_input_manager.get(),
                  'oid': manage_id
              })

    db_connect.commit()
    db_connect.close()
    manager.destroy()

def manage():
    manage_id = manage_id_input.get()
    #print(manage_id)

    if len(manage_id) == 0:
        return
    global manager
    global price_input_manager
    global symbol_input_manager



    manager = tk.Tk()
    manager.title("SYMBOL MANAGER")
    manager.geometry(MANAGER_GEOMETRY_SIZE)



    db_connect = sqlite3.connect(DB_NAME)
    c = db_connect.cursor()

    c.execute(f"SELECT * FROM {TABLE_NAME} WHERE oid=" + manage_id)
    records = c.fetchall() # fetches all records

    # Create Labels
    symbol_manager = tk.Label(manager, text="SYMBOL", width=15)
    symbol_manager.grid(row=0,column=0)
    target_price_manager = tk.Label(manager, text="ALERT PRICE", width=15)
    target_price_manager.grid(row=1,column=0)

    # Create Entry
    symbol_input_manager = tk.Entry(manager, width=10)
    symbol_input_manager.grid(row=0, column=1, pady=10)
    price_input_manager = tk.Entry(manager, width=10)
    price_input_manager.grid(row=1,column=1, pady=10)

    # Save Change Button in Manager
    save_change_btn = tk.Button(manager, text="SAVE CHANGES", command=save_change, width=20)
    save_change_btn.grid(row=3, column=0, pady=10, columnspan=2)
    del_btn = tk.Button(manager, text="DELETE", command=delete, width=20)
    del_btn.grid(row=4, column=0, pady=10, columnspan=2)

    # Loop through results
    for record in records:
        symbol_input_manager.insert(0, record[0])
        price_input_manager.insert(0, record[1])

    manage_id_input.delete(0, tk.END)

def query():
    db_connect = sqlite3.connect(DB_NAME)
    c = db_connect.cursor()

    c.execute(f"SELECT *, oid FROM {TABLE_NAME}")
    records = c.fetchall() # fetches all records

    # Display Treeview
    my_tree = ttk.Treeview(root)

    # Define Columns
    my_tree['columns'] = ("ID", "SYMBOL", "ALERT PRICE", "CURRENT PRICE")

    # Format Columns
    my_tree.column("#0", width=0, stretch=tk.NO)
    my_tree.column("ID", anchor=tk.CENTER, width=60)
    my_tree.column("SYMBOL", anchor=tk.CENTER, width=100)
    my_tree.column("ALERT PRICE", anchor=tk.CENTER, width=100)
    my_tree.column("CURRENT PRICE", anchor=tk.CENTER, width=100)

    # Create Headings
    my_tree.heading("#0", text="", anchor=tk.CENTER)
    my_tree.heading("ID", text="ID", anchor=tk.CENTER)
    my_tree.heading("SYMBOL", text="SYMBOL", anchor=tk.CENTER)
    my_tree.heading("ALERT PRICE", text="ALERT PRICE", anchor=tk.CENTER)
    my_tree.heading("CURRENT PRICE", text="CURRENT PRICE", anchor=tk.CENTER)

    # Add Data
    for i in range(len(records)):
        symbol_name= records[i][0]
        tPrice = records[i][1]
        currPrice = records[i][2]
        my_tree.insert(parent='', index='end', iid=i, text="", values=(i+1, symbol_name, tPrice, currPrice))

    my_tree.grid(row=5, column=0, columnspan=4, padx=10)
    db_connect.close()



def export():
    db_connect = sqlite3.connect(DB_NAME)
    c = db_connect.cursor()

    c.execute(f"SELECT * FROM {TABLE_NAME}")
    data = c.fetchall()
    return data

def refresh():
    pass

if __name__ == '__main__':

    root = tk.Tk()
    root.title("PY STOCK PRICE ALERT")
    root.geometry(ROOT_GEOMETRY_SIZE)

    # Create Labels
    symbol = tk.Label(root, text="STOCK SYMBOL", width=15)
    symbol.grid(row=0,column=0, pady=10)
    target_price = tk.Label(root, text="ALERT PRICE", width=15)
    target_price.grid(row=1,column=0, pady=10)
    manage_id_label = tk.Label(root, text="SYMBOL ID", width=15)
    manage_id_label.grid(row=3, column=0, pady=10)

    # Create Entry
    symbol_input = tk.Entry(root, width=20)
    symbol_input.grid(row=0, column=1)
    price_input = tk.Entry(root, width=20)
    price_input.grid(row=1,column=1)
    manage_id_input = tk.Entry(root, width=20)
    manage_id_input.grid(row=3, column=1)

    # Create Buttons
    addButton = tk.Button(root, text="ADD SYMBOL & PRICE", command=add, width=50)
    addButton.grid(row=2,column=0, columnspan=2, padx=10, pady=5)
    manage_btn = tk.Button(root, text="MANAGE SYMBOL ID", command=manage, width=50)
    manage_btn.grid(row=4, column=0, columnspan=2, padx=10, pady=5)
    refresh_btn = tk.Button(root, text="REFRESH TABLE", command=query, width=50)
    refresh_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

    query()

    root.mainloop()



