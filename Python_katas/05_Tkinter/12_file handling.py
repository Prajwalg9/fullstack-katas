import tkinter as tk
from tkinter import filedialog
from tkinter import ttk



def save():
    data=textarea.get("1.0","end-1c")
    filename=filedialog.asksaveasfile(filetypes=(("Text File","*.txt"),("All Files","*.*")))
    if filename:
        filename.write(data)
        filename.close()



root = tk.Tk()
root.title("Text Area")
root.config(background="cyan")
root.geometry("700x600")

textarea=tk.Text(root,bg="white",fg="black",width=70,height=20,padx=5,pady=5)
textarea.pack()


backspace=ttk.Button(root,
                     text="Backspace",
                     padding=2,
                     command=lambda: textarea.delete("end-2c","end-1c"),
                     )
backspace.pack(anchor="w")
backspace.place(x=30,y=370)
submit=tk.Button(root,
                 text="Submit",
)


Clear=ttk.Button(root,
                text="Clear",
                padding=2,
                command=lambda: textarea.delete("1.0","end"),
                )
Clear.pack(anchor="w")
Clear.place(x=130,y=370)

save=ttk.Button(root,
               text="Save",
               padding=2,
               command=save
               )
save.pack()
save.place(x=230,y=370)

root.mainloop()