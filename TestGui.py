import tkinter
import tkinter as tk
import csv
from tkinter import font
import pandas as pd
from tkinter import ttk
from ttkthemes import ThemedTk

root = tk.Tk()

data= pd.read_csv("stockprices.csv")
data
data.columns
data.Company
data.Price
data.Change

ThemedTk(theme="equilux")
#naming the gui window
root.title('Stocks')
root.geometry("400x250")
#Showing the data from the csv
w = tk.Label(root, text=(data))


w.pack()
root.mainloop()