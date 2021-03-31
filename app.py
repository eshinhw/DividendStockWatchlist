import tkinter as tk
from tkinter import filedialog, Text
import os
import sqlite3

root = tk.Tk()
root.title("Stock Price Alert")
root.geometry("800x800")
def journal():
    symbol = symbol_input.get()
    price = price_input.get()

    sp = tk.Label(root, text=f"You entered {symbol} at {price}")
    sp.pack()

# canvas = tk.Canvas(root, height=500, width=500, bg="#263D42")
# canvas.pack()

symbol = tk.Label(root, text="Symbol: ")
symbol.grid(row=0,column=0)
symbol_input = tk.Entry()
symbol_input.grid(row=0, column=1)

target_price = tk.Label(root, text="Target Price: ")
target_price.grid(row=0,column=2)
price_input = tk.Entry()
price_input.grid(row=0,column=3)

addButton = tk.Button(root, text="Add", padx=45, command=journal)
addButton.grid(row=0,column=4)

# Database

# Create a database or connect to one
conn = sqlite3.connect('price_alert.db')

# Create a cursor
c = conn.cursor()





# Commit changes
conn.commit()

# Close connection
conn.close()




height = 5
width = 3
for i in range(1, height): #Rows
    for j in range(width): #Columns
        if (i == 1): # header of the table
            if j == 0:
                symbol_header = tk.Label(root, text="Symbol")
                symbol_header.grid(row=i, column=j)
                continue
            if j == 1:
                target = tk.Label(root, text="Target Price")
                target.grid(row=i, column=j)
                continue
            if j == 2:
                current = tk.Label(root, text="Current Price")
                current.grid(row=i, column=j)
                continue

        content = tk.Label(root, text="abc")
        content.grid(row=i, column=j)



root.mainloop()