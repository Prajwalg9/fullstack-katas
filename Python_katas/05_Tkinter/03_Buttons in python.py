import tkinter as tk
from tkinter import PhotoImage

counter=0
def click():
    global counter
    counter=counter+1
    print(counter)


root = tk.Tk()

Like=PhotoImage(file="Like.png")

button = tk.Button(root,
                   text="Click me", #text inside
                   font=("Comic Sans", 20, "bold"), #font specification
                   fg="white", #font color
                   bg="blue", #background color
                   command=click,

                   activebackground="green", #on click
                   activeforeground="black", #on click
                   state="active", #Access

                   image=Like, #adding image
                   compound="left", #align it
                   padx=10, #paddings
                   pady=10, #paddings
                   )
button.pack()

root.mainloop()