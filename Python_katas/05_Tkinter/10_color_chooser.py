import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser

def color():
    color= colorchooser.askcolor()
    root.config(bg=color[1])

root = tk.Tk()
root.title('Color')
root.geometry('300x300')

button=ttk.Button(root,text='Select Color', command=color)
button.pack()

root.mainloop()