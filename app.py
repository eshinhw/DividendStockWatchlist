import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
root.title("Stock Price Alert")
root.geometry("500x500")
# def get_input():
#     symbol = symbol_input.get()
#     price = price_input.get()

#     sp = tk.Label(root, text=f"You entered {symbol} at {price}")
#     sp.pack()

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

addButton = tk.Button(root, text="Add", padx=45)
addButton.grid(row=0,column=4)


root.mainloop()