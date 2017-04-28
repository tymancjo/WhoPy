# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tkinter as tk

def papa():
    print('PaPa')
    root.destroy()
    
def napis(*arg):
    print('mysz się rusza')
 
root = tk.Tk()
 
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

Klawisz = tk.Button(frame, text = 'Knefel 1', width = 25).grid(column=0, row=0, columnspan=4)

Klawisz = tk.Button(frame, text = 'Knefel 2').grid(column=1, row=1)

Klawisz = tk.Button(frame, text = 'Knefel X', command = papa).grid(column=2, row=2)

Klawisz = tk.Button(frame, text = 'Knefel Z', height = 30).grid(column=3, row=1, rowspan = 3)

frame.bind("<B1-Motion>", napis)


root.mainloop()