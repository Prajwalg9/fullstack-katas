import tkinter as tk

def new_window():
    window=tk.Tk()
    window.geometry("300x100")
    window.title("New Window")
    tk.Label(window,text="New Window").pack(side="top")

root=tk.Tk()
root.title("Sub Window")
root.geometry("500x500")

tk.Button(root,text="Create new widow", command=new_window).pack()

root.mainloop()