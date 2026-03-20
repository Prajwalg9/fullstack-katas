import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk()
root.geometry("700x700")

image=PhotoImage(file="logo.png")

label = tk.Label(root,
                 text="My Logo",
                 fg="white",#text color
                 bg="green",#background color
                 font=("Arial", 30, "bold"),#font specifications
                 relief="raised",#border behaviour
                 bd=10,#border
                 padx=10,pady=10,#paddings
                 image=image,#add image with label
                 compound="bottom"#align image with logo
                 )
label.pack()
label.place(x=100,y=100)#change place of label

label.mainloop()