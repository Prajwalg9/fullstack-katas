import tkinter as tk

def new():
    print("New File")
def Open():
    print("Open File")
def Cut():
    print("Cut")
def Paste():
    print("Paste")

root = tk.Tk()
root.title("Menu Bar")
root.geometry("500x400")

menubar = tk.Menu(root)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=new)
filemenu.add_command(label="Open", command=Open)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=quit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=Cut)
editmenu.add_command(label="Copy", command=Open)
editmenu.add_command(label="Paste", command=Paste)
menubar.add_cascade(label="Edit", menu=editmenu)

root.config(menu=menubar)
root.mainloop()