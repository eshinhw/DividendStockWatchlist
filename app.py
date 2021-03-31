import os
import sqlite3
import tkinter as tk
import datetime as dt
import pandas_datareader.data as web

# from tkinter import ttk

DB_NAME = 'price_alert.db'
TABLE_NAME = 'price_data'
GEOMETRY_SIZE = '400x600'

def _get_close_price(symbol):
    startDate = (dt.date.today() - dt.timedelta(days=1)).strftime("%Y-%m-%d")
    endDate = dt.date.today().strftime("%Y-%m-%d")
    close = web.DataReader(symbol, 'yahoo', startDate, endDate)['Adj Close'].iloc[-1].round(2)
    return close

def _clear_input():
    symbol_input.delete(0, tk.END)
    price_input.delete(0, tk.END)


def add():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Create a table
    c.execute(f"""CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        symbol text,
        target_price real,
        current_price real
        ) """
              )
    # INPUT VALIDITY CHECK
    s = symbol_input.get()
    tp = price_input.get()
    if (s == "") or (not str(tp).isnumeric()):
        _clear_input()
        return
    try:
        cp = _get_close_price(s)
    except:
        _clear_input()
        return

    # Insert into table
    c.execute(f"INSERT INTO {TABLE_NAME} VALUES (:symbol, :target_price, :current_price)",
              {
                  'symbol': s.upper(),
                  'target_price': tp,
                  'current_price': cp
              })

    _clear_input()
    conn.commit()
    conn.close()

def delete():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute(f"DELETE from {TABLE_NAME} WHERE oid=" + select_record.get())
    delete_record.delete(0, tk.END)

    conn.commit()
    conn.close()

def save_change():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    select_id = select_record.get()

    c.execute(f"""UPDATE {TABLE_NAME} SET
              symbol = :s,
              target_price = :tp

              WHERE oid = :oid
              """,
              {
                  's': symbol_input_editor.get(),
                  'tp': price_input_editor.get(),
                  'oid': select_id
              })

    conn.commit()
    conn.close()
    editor.destroy()

def edit():
    global editor
    editor = tk.Tk()
    editor.title("Stock Price Alert")
    editor.geometry(GEOMETRY_SIZE)

    edit_id = select_record.get()


    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute(f"SELECT * FROM {TABLE_NAME} WHERE oid=" + edit_id)
    records = c.fetchall() # fetches all records

    # Create Labels
    symbol_editor = tk.Label(editor, text="Symbol", width=10)
    symbol_editor.grid(row=0,column=0)
    target_price_editor = tk.Label(editor, text="Target Price", width=10)
    target_price_editor.grid(row=1,column=0)

    global symbol_input_editor
    global price_input_editor

    # Create Entry
    symbol_input_editor = tk.Entry(editor)
    symbol_input_editor.grid(row=0, column=1)
    price_input_editor = tk.Entry(editor)
    price_input_editor.grid(row=1,column=1)

    save_change_btn = tk.Button(editor, text="SAVE CHANGE", command=save_change, width=20)
    save_change_btn.grid(row=3, column=0, pady=10, columnspan=2)

    # Loop through results
    for record in records:
        symbol_input_editor.insert(0, record[0])
        price_input_editor.insert(0, record[1])

def query():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute(f"SELECT *, oid FROM {TABLE_NAME}")
    records = c.fetchall() # fetches all records
    output_records = ""
    for record in records:
        print(record)
        output_records += str(record[3]) + '\t' + str(record[0]) + '\t' + str(record[1]) + '\t' + str(record[2]) + '\n'

    outputLabel = tk.Label(root, text=output_records)
    outputLabel.grid(row=8, column=0)

    conn.close()

def export():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute(f"SELECT * FROM {TABLE_NAME}")
    data = c.fetchall()
    return data

def refresh():
    pass

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Stock Price Alert")
    root.geometry(GEOMETRY_SIZE)
    # Create Labels
    symbol = tk.Label(root, text="Symbol", width=10)
    symbol.grid(row=0,column=0)
    target_price = tk.Label(root, text="Target Price", width=10)
    target_price.grid(row=1,column=0)
    select_label = tk.Label(root, text="Select ID", width=10)
    select_label.grid(row=5, column=0)

    # Create Entry
    symbol_input = tk.Entry()
    symbol_input.grid(row=0, column=1)
    price_input = tk.Entry()
    price_input.grid(row=1,column=1)
    select_record = tk.Entry()
    select_record.grid(row=5, column=1)

    # Create Buttons
    addButton = tk.Button(root, text="ADD", command=add, width=30)
    addButton.grid(row=3,column=0, pady=10, columnspan=2)
    query_btn = tk.Button(root, text="QUERY", command=query, width=20)
    query_btn.grid(row=4, column=0, pady=10, columnspan=2)
    del_btn = tk.Button(root, text="DELETE", command=delete, width=20)
    del_btn.grid(row=6, column=0, pady=10, columnspan=2)
    update_btn = tk.Button(root, text="UPDATE", command=edit, width=20)
    update_btn.grid(row=7, column=0, pady=10, columnspan=2)
    # query_header = tk.Label(root, text="Symbol" + '\t' +"Target Price")
    # query_header.grid(row=7, column=0)


    # tree = ttk.Treeview(root, column=("c1", "c2"), show='headings')
    # tree.column("#1", anchor=tk.CENTER)

    # tree.heading("#1", text="SYMBOL")

    # tree.column("#2", anchor=tk.CENTER)

    # tree.heading("#2", text="TARGET")

    # tree.grid(row=2, column=0, columnspan=6)



    root.mainloop()