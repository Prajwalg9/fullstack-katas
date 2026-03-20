import tkinter as tk

from click import command

root = tk.Tk()
root.geometry("500x500")
root.title("Check-Box")

def check():
    print(x.get())

#we can add image to our check box

x= tk.StringVar()

checkbox = tk.Checkbutton(root,
                          text="Are you agree to terms and conditions?",
                          variable=x,
                          fg="black",bg="Magenta",font=("Times New Roman",20),
                          onvalue="Agreed to terms and conditions",
                          offvalue="Not agreed to terms and conditions",
                          command=check
                          )
checkbox.pack()


root.mainloop()