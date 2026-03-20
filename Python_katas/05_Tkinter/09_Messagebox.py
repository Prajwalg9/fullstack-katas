import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def info():
    messagebox.showinfo(title='Info', message='You are a person.')

def warn():
    messagebox.showwarning(title='Warning', message='What are you doing here? Go home!')

def error_msg():
    messagebox.showerror(title='Error!', message='Sorry, try again.')

def ask_ok_cancel():
    if messagebox.askokcancel(title='Ok or Cancel?', message='Proceed with this action?'):
        print("Ok")
    else:
        print("Cancel")

def ask_yes_no():
    if messagebox.askyesno(title='Yes or No?', message='Do you like Tkinter?'):
        print("Yes")
    else:
        print("No")

def ask_retry_cancel():
    if messagebox.askretrycancel(title='Retry or Cancel?', message='Operation failed. Retry?'):
        print("retry")
    else:
        print("cancel")

def ask_question():
    result = messagebox.askquestion(title='Question', message='Do you want to continue?')
    print(result)  # 'yes' or 'no'

def ask_yes_no_cancel():
    result = messagebox.askyesnocancel(title='Yes / No / Cancel',
                                       message='Save changes before exiting?')
    print(result)  # True, False, or None

root = tk.Tk()
root.title("Messagebox")
root.geometry("400x400")

info_btn = ttk.Button(root, text="Info", command=info)
info_btn.pack(pady=5)

warn_btn = ttk.Button(root, text="Warning", command=warn)
warn_btn.pack(pady=5)

error_btn = ttk.Button(root, text="Error", command=error_msg)
error_btn.pack(pady=5)

ok_cancel_btn = ttk.Button(root, text="askokcancel", command=ask_ok_cancel)
ok_cancel_btn.pack(pady=5)

yes_no_btn = ttk.Button(root, text="askyesno", command=ask_yes_no)
yes_no_btn.pack(pady=5)

retry_cancel_btn = ttk.Button(root, text="askretrycancel", command=ask_retry_cancel)
retry_cancel_btn.pack(pady=5)

ask_question_btn = ttk.Button(root, text="askquestion", command=ask_question)
ask_question_btn.pack(pady=5)

yes_no_cancel_btn = ttk.Button(root, text="askyesnocancel", command=ask_yes_no_cancel)
yes_no_cancel_btn.pack(pady=5)

root.mainloop()
