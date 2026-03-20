import tkinter as tk
from tkinter import ttk

root= tk.Tk()
root.title("tabs")
root.geometry("500x400")

notebook = ttk.Notebook(root)
notebook.pack(fill="both",expand=True)

tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)

notebook.add(tab1,text="Notebook tab 1")
notebook.add(tab2,text="Notebook tab 2")
notebook.add(tab3,text="Notebook tab 3")

label1 = tk.Label(tab1,text="Tab 1")
label2 = tk.Label(tab2,text="Tab 2")
label3 = tk.Label(tab3,text="Tab 3")
label1.pack()
label2.pack()
label3.pack()

root.mainloop()