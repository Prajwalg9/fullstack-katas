import tkinter as tk
from tkinter import PhotoImage


def order():
    print(f"Order: {food[x.get()]}")

root = tk.Tk()
root.title("Radio Button")
root.geometry("650x500")

food=["Pizza","Burger","Pasta","Frech_fries"]
x= tk.IntVar()
images=[]

for item in range(len(food)):
    image=PhotoImage(file=f"{food[item]}.png")
    images.append(image)
    radio=tk.Radiobutton(root,
                         text=food[item],value=item,
                         variable=x,
                         font=("Impact",20),
                         padx=10,pady=10,
                         command=order,
                         image=image,
                         compound="left"
                         )
    radio.pack(anchor="nw") #|   e|,  |w   |,|nw  ne|  {north, east, west, south
root.mainloop()