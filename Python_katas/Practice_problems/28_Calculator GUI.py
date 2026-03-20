import tkinter as tk

expression=""
def press(num):
    global expression
    expression += str(num)
    Text.set(expression)


def calc():
    global expression
    try:
        result = str(eval(expression))
        Text.set(result)
        expression = ""
    except:
        Text.set("Error")
        expression = ""

def clear():
    global expression
    Text.set("")
    expression = ""

root = tk.Tk()
root.title("Calculator")
root.geometry("300x410")
root.config(bg="#0e0180")
root.resizable(False, False)

Text= tk.StringVar()

entry = tk.Entry(root, textvariable=Text)
entry.pack(fill="x",pady=10, padx=10, ipady=10)

buttons=[
    ("7",1,0),("8",1,1),("9",1,2),("/",1,3),
    ("4",2,0),("5",2,1),("6",2,2),("*",2,3),
    ("1",3,0),("2",3,1),("3",3,2),("-",3,3),
    ("0",4,0),(".",4,1),("=",4,2),("+",4,3)
]

Btn=tk.Frame(root,pady=10)
Btn.pack()
Btn.config(bg="#0e0180")
for text,row,col in buttons:
    if text=="=":
        btn = tk.Button(Btn, text=text, bg="magenta",bd=0, fg="white", font=("Arial", 14), command=calc, width=5, height=2)
    else:
        btn = tk.Button(Btn, text=text, bg="black",bd=0, fg="white", font=("Arial", 14), command=lambda t=text: press(t), width=5, height=2)
    btn.grid(column=col,row=row,padx=5,pady=5)

Clear=tk.Button(root, text="Clear", command=clear, height=2,padx=5,pady=5,bg="red",fg="white", font=("Arial", 14), width=5)
Clear.pack(expand=True,fill="x")

root.mainloop()