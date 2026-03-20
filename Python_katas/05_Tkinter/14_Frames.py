import tkinter as tk

root = tk.Tk()
root.title("Frame")
root.geometry("400x400")

frame=tk.Frame(root,bg="pink")
frame.pack(side="bottom")

tk.Button(frame,text="W").pack(side="top")
tk.Button(frame,text="X").pack(side="left")
tk.Button(frame,text="F").pack(side="left")
tk.Button(frame,text="D").pack(side="left")

root.mainloop()