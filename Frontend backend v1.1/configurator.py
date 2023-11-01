from tkinter import *
from cfg import new_print
import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import threading
root = tk.Tk()
root.title("Car Dashboard Configurator")
root.geometry("600x400")
root.configure(bg='white')
def main():
        new_print(entry.get(), bitrates_combo.get(),projects_combo.get(),devices_combo.get())
def chooseinputfile1():
    global dbcfilename
    dbcfilename = filedialog.askopenfilename(title='Open DBC', filetypes=[('DBC', '*.dbc'), ('All Files', '*')])
    inputfilepath1.set(dbcfilename)
interface = Label(root, text = "Select Interface Device :").place(x = 11,y = 13)
devices = ["pcan", "Vector"]
devices_combo = ttk.Combobox(root, values=devices)
devices_combo.place(width = 150, x=140, y=13)
project = Label(root, text = "Select Project :").place(x=58, y = 43)
projects = ["TML", "Mahindra", "Bajaj", "Suzuki"]
projects_combo = ttk.Combobox(root, values=projects) 
projects_combo.place(width=150, x=140, y=43)
bitrate = Label(root, text = "Select Bitrate :").place(x=61, y = 73)
bitrates = ["125 kbps","250 kbps","500 kbps","1000 kbps"]
bitrates_combo = ttk.Combobox(root, values=bitrates)
bitrates_combo.place(width=150, x=140, y=73)
inputfilepath1 = StringVar()
inputfilepath1.set('')
Label(root,text = "Selected DBC:").place(x=60, y=103)
entry = Entry(root, textvariable=inputfilepath1)
entry.place(width = 250, x=140,y=103)
Button(root, text = "Select DBC", command = chooseinputfile1).place(x=370, y=103)
apply_button = ttk.Button(root, text="Apply", command=main).place(x= 135, y=150)
exit_button = ttk.Button(root, text="Exit", command=root.destroy).place(x= 215, y=150)
threading.Thread(target = main, args = entry.get(),).start()
root.mainloop()