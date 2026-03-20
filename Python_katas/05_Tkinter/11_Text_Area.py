import tkinter as tk
from tkinter import ttk

def submit():
    input = text.get("1.0","end")
    label.config(text=input)

root = tk.Tk()
root.title("Text Area")
root.geometry("400x300")

label = tk.Label(root, text="Text Area",bg="yellow",padx=10, pady=10)
label.pack()


text= tk.Text(root, height=2, width=20
              ,padx=10, pady=10
              ,fg="purple",
              bg="limegreen"
              )
text.pack()

button = ttk.Button(root, text="Submit", command=submit)
button.pack()
root.mainloop()



root.mainloop()