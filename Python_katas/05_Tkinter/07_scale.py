import tkinter as tk

from PIL.ImageTk import PhotoImage
def submit():
    value_label.config(text=f"Temperature: {scale.get()}°C")

root = tk.Tk()
root.title("Scale")
root.geometry("200x635")

hot=PhotoImage(file="hot.png")
hotL=tk.Label(root,image=hot)
hotL.pack(anchor="w")

scale = tk.Scale(root,
              from_=100, #sterting
              to=0, #till
              orient=tk.VERTICAL, #orientation
              fg="cyan", #textcolor
              bg="#000005", #background
              length=500, #Height
              tickinterval=5, #show ruler
              showvalue=False   #Hide scale values
              )
scale.pack(anchor="w")
cold=PhotoImage(file="cold.png")
coldL=tk.Label(root,image=cold)
coldL.pack(anchor="w")

button=tk.Button(root,text="Click Me",command=submit)
button.pack(anchor="w")

value_label = tk.Label(root, text="Temperature: --°C", font=("Times New Roman", 20))
value_label.pack(anchor="w")

root.mainloop()