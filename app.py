from tkinter import ttk
import tkinter as tk
from tkinter import filedialog, Text
import os
import sqlite3

root = tk.Tk()
root.title("Stock Price Alert")
root.geometry("800x800")

def add():

    conn = sqlite3.connect('price_alert.db')
    c = conn.cursor()

    # Create a table

    c.execute("""CREATE TABLE IF NOT EXISTS prices_v2 (
        symbol text,
        target_price real
        ) """
              )

    # Insert into table

    c.execute("INSERT INTO prices_v2 VALUES (:symbol, :target_price)",
              {
                  'symbol': symbol_input.get(),
                  'target_price': price_input.get()
              })

    symbol_input.delete(0, tk.END)
    price_input.delete(0, tk.END)
    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

def query():
    conn = sqlite3.connect('price_alert.db')
    c = conn.cursor()

    c.execute("SELECT *, oid FROM prices_v2")
    records = c.fetchall() # fetches all records

    for record in records:
        print(record)
        tree.insert("", tk.END, values=record)

    # Close connection
    conn.close()



symbol = tk.Label(root, text="Symbol: ")
symbol.grid(row=0,column=0)
symbol_input = tk.Entry()
symbol_input.grid(row=0, column=1)

target_price = tk.Label(root, text="Target Price: ")
target_price.grid(row=0,column=2)
price_input = tk.Entry()
price_input.grid(row=0,column=3)

addButton = tk.Button(root, text="Add", padx=45, command=add)
addButton.grid(row=0,column=4)

query_btn = tk.Button(root, text="Query", command=query)
query_btn.grid(row=0, column=5, columnspan=2)


tree = ttk.Treeview(root, column=("c1", "c2"), show='headings')
tree.column("#1", anchor=tk.CENTER)

tree.heading("#1", text="SYMBOL")

tree.column("#2", anchor=tk.CENTER)

tree.heading("#2", text="TARGET")

tree.grid(row=2, column=3)



root.mainloop()