import tkinter as tk
from tkinter import PhotoImage

root=tk.Tk()
root.title("My First GUI App")#Title of app
root.geometry("400x400")#size of window

logo=PhotoImage(file="logo.png")#logo of app
root.iconphoto(True,logo)

root.configure(bg="Purple")#Background color

label=tk.Label(root,text="Hello, World!", font=("Arial", 10, "bold"),bg="Limegreen",fg="brown")
label.pack()

root.mainloop()