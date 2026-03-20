import tkinter as tk
from multiprocessing.managers import State
from tkinter import Listbox


def add():
    Listbox2.config(state="normal")
    Listbox2.insert(Listbox.size(),Listbox.get(Listbox.curselection()))
    Listbox2.config(state=tk.DISABLED)
def delete():
    Listbox.delete(Listbox.curselection())
    Listbox.config(height=Listbox.size())
def addM():
    Listbox.insert(Listbox.size(),var.get())
    Listbox.config(height=Listbox.size())

root = tk.Tk()
root.title("Listbox")
root.geometry("650x500")
root.configure(bg="Purple")

Listbox = tk.Listbox(root,bg="cyan")
Listbox.place(x=15,y=15)
Listbox.config(height=Listbox.size())

Listbox.insert(1,"Pizza")
Listbox.insert(2,"burger")
Listbox.insert(3,"Fresh Frise")
Listbox.insert(4,"cheese")
Listbox.insert(5,"Panir chilly")
Listbox.insert(6,"Soya chungs")

Listbox2=tk.Listbox(root,bg="Blue",fg="black")
Listbox2.pack()
Listbox2.config(height=Listbox2.size(),state=tk.DISABLED)
Listbox2.place(x=350,y=20)

add=tk.Button(root,text="Submit  =>",command=add)
add.pack()
add.place(x=170,y=25)

delete=tk.Button(root,text="<=  Delete Menu Option",command=delete)
delete.pack()
delete.place(x=170,y=60)

var=tk.StringVar()
Entry=tk.Entry(root,textvariable=var)
Entry.pack()
Entry.place(x=170,y=95)

addM=tk.Button(root,text="<=  Add to menu>",command=addM)
addM.pack()
addM.place(x=170,y=130)




root.mainloop()