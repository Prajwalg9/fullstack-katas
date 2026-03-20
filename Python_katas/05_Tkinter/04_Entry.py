import tkinter as tk

from Demos.win32ts_logoff_disconnected import username

root = tk.Tk()
root.geometry("500x500")
root.title("Entry")

def submit():
    username=entry.get()
    print(f"Hello, {username}!")

def clear():
    entry.delete(0,"end")

def backspace():
    entry.delete(len(entry.get())-1,"end")



entry = tk.Entry(root,
                 width=50, font=("Arial",20),
                 fg="black", bg="lightblue", bd=10, justify="center"
                 )
entry.pack()

submit=tk.Button(root,text="Submit",command=submit)
submit.pack()
backspace = tk.Button(root,text="Backspace",command=backspace)
backspace.pack()
clear = tk.Button(root,text="Clear",command=clear)
clear.pack()

root.mainloop()