import tkinter as tk
from tkinter import *
import sqlite3

my_conn = sqlite3.connect('stform3.db')

my_w = tk.Tk()
my_w.geometry("1300x250")
my_w.title("Database")
r_set = my_conn.execute('''SELECT * from STFORM3 ''')
for i, STFORM3 in enumerate(r_set):
    for j in range(len(STFORM3)):
        e = Entry(my_w, width=10, fg='black')
        e.grid(row=i, column=j)
        e.insert(END, STFORM3[j])
my_w.mainloop()
