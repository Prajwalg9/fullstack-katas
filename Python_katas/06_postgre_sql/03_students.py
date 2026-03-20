import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import psycopg2
import csv

conn = psycopg2.connect(dbname="collage", user="postgres",password="viru",host="localhost",port="1800")
cursor = conn.cursor()


root = tk.Tk()
root.title("Students Registration System")
root.geometry("600x550")
root.resizable(False,False)

# ---------- CLEAR SCREEN ----------
def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()

# ---------- STUDENT SCREEN ----------
def student():
    clear_screen()

    std = tk.Frame(root)
    std.pack(fill="both", expand=True, padx=30, pady=20)
    
    tk.Label(
        std, text="• 👨‍🎓 Student Login •",
        font=("Arial", 16, "bold"),
        bg="darkblue", fg="white",
        pady=12
    ).pack(fill="x", pady=(0, 20))

    roll = tk.StringVar()
    passwd = tk.StringVar()

    ttk.Label(std, text="Roll Number").pack(anchor="w")
    ttk.Entry(std, textvariable=roll).pack(fill="x", pady=5,ipady=10)

    ttk.Label(std, text="Password").pack(anchor="w")
    ttk.Entry(std, textvariable=passwd, show="*").pack(fill="x", pady=5,ipady=10)

    ttk.Button(
        std, text="Login",
        command=lambda: student_login(roll.get(), passwd.get())
    ).pack(pady=15)

    ttk.Button(std, text="Back", command=main_screen).pack()

def student_login(roll, passwd):
    if not roll or not passwd:
        messagebox.showerror("Error", "All fields required")
        return

    cursor.execute(
        "SELECT roll_no FROM students WHERE roll_no=%s AND password=%s",
        (roll, passwd)
    )
    result = cursor.fetchone()

    if result:
        student_dashboard(roll)
    else:
        messagebox.showerror("Error", "Invalid Roll Number or Password")

def student_dashboard(roll):
    clear_screen()

    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True, padx=30, pady=20)

    tk.Label(
        frame, text="• 👋 welcome Student •",
        font=("Arial", 16, "bold"),
        bg="darkgreen", fg="white",
        pady=12
    ).pack(fill="x", pady=(0, 20))

    ttk.Button(
        frame, text="👤 View My Profile",
        command=lambda: view_profile(roll),
        padding=10
    ).pack(pady=8, fill="x")

    ttk.Button(
        frame, text="🔑 Change Password",
        command=lambda: change_student_password(roll),
        padding=10
    ).pack(pady=8, fill="x")

    ttk.Button(
        frame, text="🏠 Logout",
        command=main_screen,
        padding=10
    ).pack(pady=8, fill="x")

def view_profile(roll):
    clear_screen()

    frame = tk.Frame(root)
    frame.pack(padx=30, pady=20)

    tk.Label(frame, text="👤 My Profile", font=("Arial", 14, "bold")).pack(pady=10)

    cursor.execute(
        "SELECT roll_no, name, age, course, phone, email FROM students WHERE roll_no=%s",
        (roll,)
    )
    row = cursor.fetchone()

    labels = ["Roll No", "Name", "Age", "Course", "Phone", "Email"]

    for i, value in enumerate(row):
        tk.Label(frame, text=f"{labels[i]}: {value}", font=("Arial", 11)).pack(anchor="w", pady=2)

    ttk.Button(frame, text="Back", command=lambda: student_dashboard(roll)).pack(pady=15)

def change_student_password(roll):
    clear_screen()

    frame = tk.Frame(root)
    frame.pack(padx=30, pady=20)

    tk.Label(frame, text="🔑 Change Password", font=("Arial", 14, "bold")).pack(pady=10)

    old = tk.StringVar()
    new = tk.StringVar()

    ttk.Label(frame, text="Old Password").pack(anchor="w")
    ttk.Entry(frame, textvariable=old, show="*").pack(fill="x", pady=5)

    ttk.Label(frame, text="New Password").pack(anchor="w")
    ttk.Entry(frame, textvariable=new, show="*").pack(fill="x", pady=5)

    def change():
        cursor.execute(
            "SELECT password FROM students WHERE roll_no=%s",
            (roll,)
        )
        current = cursor.fetchone()[0]

        if old.get() != current:
            messagebox.showerror("Error", "Old password incorrect")
            return

        cursor.execute(
            "UPDATE students SET password=%s WHERE roll_no=%s",
            (new.get(), roll)
        )
        conn.commit()
        messagebox.showinfo("Success", "Password updated successfully")
        student_dashboard(roll)

    ttk.Button(frame, text="Update Password", command=change).pack(pady=10)
    ttk.Button(frame, text="Back", command=lambda: student_dashboard(roll)).pack()


# ---------- ADMIN SCREEN ----------
def administrator():
    clear_screen()
    admin = tk.Frame(root)
    admin.pack(fill="both", expand=True)
    

    tk.Label(
        admin, text="• welcome Administrator •",
        font=("Arial", 15, "bold"),
        bg="darkblue", fg="white",
        pady=10
    ).pack(fill="x")

    tk.Label(
        admin, text="Admin Login",
        font=("Arial", 13, "bold"),
        pady=10
    ).pack()

    tk.Label(admin, text="Admin Password").pack(anchor="w", padx=20)
    passwd = tk.StringVar()
    Passwd = ttk.Entry(admin, textvariable=passwd, show="*")
    Passwd.pack(padx=20, pady=8, ipady=10,fill="x")

    btn=ttk.Button(admin, text="Submit", command=lambda: Submit(passwd.get()))
    btn.pack(pady=15,padx=15)
    back=ttk.Button(admin, text="Back", command=main_screen)
    back.pack(pady=15,padx=15)
    
def add_std():
    clear_screen()
    

    admin = tk.Frame(root)
    admin.pack(fill="both", expand=True, padx=20, pady=10)

    tk.Label(
        admin, text="• Add Student •",
        font=("Arial", 15, "bold"),
        bg="darkblue", fg="white",
        pady=10
    ).pack(fill="x", pady=(0, 15))

    form = tk.Frame(admin)
    form.pack(fill="both", expand=True)

    # VARIABLES
    roll = tk.StringVar()
    name = tk.StringVar()
    passwd = tk.StringVar()
    phone = tk.StringVar()
    age = tk.StringVar()
    course = tk.StringVar()
    email = tk.StringVar()

    def field(row, col, text, var, show=None):
        tk.Label(form, text=text).grid(row=row, column=col, sticky="w", padx=10)
        ttk.Entry(form, textvariable=var, show=show).grid(
            row=row+1, column=col, padx=10,ipady=5, pady=8, sticky="ew"
        )

    form.columnconfigure(0, weight=1)
    form.columnconfigure(1, weight=1)

    # ROW 1
    field(0, 0, "Roll Number", roll)
    field(0, 1, "Name", name)

    # ROW 2
    field(2, 0, "Password", passwd, show="*")
    field(2, 1, "Phone", phone)

    # ROW 3
    field(4, 0, "Age", age)
    field(4, 1, "Course", course)

    # ROW 4
    field(6, 0, "Email (optional)", email)

    # BUTTON ROW
    btns = tk.Frame(admin)
    btns.pack(pady=20)

    def add():
        Roll=roll.get()
        Name=name.get()
        Passwd=passwd.get()
        Phone=phone.get()
        Age=age.get()
        Course=course.get()
        Email=email.get()
        if not (Roll and Name and Passwd and Phone and Age and Course):
            messagebox.showerror(
                title="Error!",
                message="All fields are required except Email!"
            )
            return

        else:
            query='''
            INSERT INTO students (roll_no, name, age, course, phone, email, password)
            VALUES (%s, %s, %s, %s, %s, %s, %s);'''
            cursor.execute(query,(Roll,Name,Age,Course,Phone,Email,Passwd))
            conn.commit()
            label.config(text="Data Inserted Succesfully!")
            
    
    label=tk.Label(admin,fg='#00ad17')
    label.pack()
        

    ttk.Button(btns, text="Submit", command=add).grid(row=0, column=0, padx=10)
    ttk.Button(btns, text="Back", command=lambda: Submit("admin")).grid(row=0, column=1, padx=10)

def show_all_students():
    clear_screen()

    admin = tk.Frame(root)
    admin.pack(fill="both", expand=True, padx=20, pady=10)

    tk.Label(
        admin, text="• All Students Data •",
        font=("Arial", 15, "bold"),
        bg="darkgreen", fg="white",
        pady=10
    ).pack(fill="x", pady=(0, 10))

    table_frame = tk.Frame(admin)
    table_frame.pack(fill="both", expand=True)

    # SCROLLBARS
    x_scroll = ttk.Scrollbar(table_frame, orient="horizontal")
    y_scroll = ttk.Scrollbar(table_frame, orient="vertical")

    columns = ("roll", "name", "age", "course", "phone", "email")

    tree = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings",
        xscrollcommand=x_scroll.set,
        yscrollcommand=y_scroll.set
    )

    x_scroll.config(command=tree.xview)
    y_scroll.config(command=tree.yview)

    x_scroll.pack(side="bottom", fill="x")
    y_scroll.pack(side="right", fill="y")
    tree.pack(fill="both", expand=True)

    # HEADINGS
    tree.heading("roll", text="Roll No")
    tree.heading("name", text="Name")
    tree.heading("age", text="Age")
    tree.heading("course", text="Course")
    tree.heading("phone", text="Phone")
    tree.heading("email", text="Email")

    # COLUMN WIDTH
    tree.column("roll", width=80, anchor="center")
    tree.column("name", width=150)
    tree.column("age", width=60, anchor="center")
    tree.column("course", width=120)
    tree.column("phone", width=120)
    tree.column("email", width=180)

    # FETCH DATA
    query = "SELECT roll_no, name, age, course, phone, email FROM students"
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", "end", values=row)

    # BACK BUTTON
    ttk.Button(
        admin,
        text="Back",
        command=lambda: Submit("admin")
    ).pack(pady=10)

def update_student():
    clear_screen()

    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    tk.Label(frame, text="✏️ Update Student", font=("Arial", 14, "bold")).pack(pady=10)

    roll = tk.StringVar()
    phone = tk.StringVar()
    course = tk.StringVar()

    ttk.Label(frame, text="Roll Number").pack()
    ttk.Entry(frame, textvariable=roll).pack()

    ttk.Label(frame, text="New Phone").pack()
    ttk.Entry(frame, textvariable=phone).pack()

    ttk.Label(frame, text="New Course").pack()
    ttk.Entry(frame, textvariable=course).pack()

    def update():
        if not roll.get():
            messagebox.showerror("Error", "Roll number required")
            return

        cursor.execute(
            "UPDATE students SET phone=%s, course=%s WHERE roll_no=%s",
            (phone.get(), course.get(), roll.get())
        )
        conn.commit()
        messagebox.showinfo("Success", "Student updated successfully")

    ttk.Button(frame, text="Update", command=update).pack(pady=5)
    ttk.Button(frame, text="Back", command=lambda: Submit("admin")).pack()



def change_admin_password():
    clear_screen()

    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    tk.Label(frame, text="🔑 Change Admin Password", font=("Arial", 14, "bold")).pack(pady=10)

    old = tk.StringVar()
    new = tk.StringVar()

    ttk.Label(frame, text="Old Password").pack()
    ttk.Entry(frame, textvariable=old, show="*").pack()

    ttk.Label(frame, text="New Password").pack()
    ttk.Entry(frame, textvariable=new, show="*").pack()

    def change():
        if old.get() != "admin":
            messagebox.showerror("Error", "Old password incorrect")
        else:
            messagebox.showinfo(
                "Success",
                "Password changed (demo only – hardcoded)"
            )

    ttk.Button(frame, text="Change Password", command=change).pack(pady=5)
    ttk.Button(frame, text="Back", command=lambda: Submit("admin")).pack()


def export_students():
    cursor.execute(
        "SELECT roll_no, name, age, course, phone, email FROM students"
    )
    rows = cursor.fetchall()

    with open("students_export.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Roll", "Name", "Age", "Course", "Phone", "Email"])
        writer.writerows(rows)

    messagebox.showinfo(
        "Exported",
        "Students exported to students_export.csv"
    )


def search_student():
    clear_screen()

    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    tk.Label(frame, text="🔍 Search Student", font=("Arial", 14, "bold")).pack(pady=10)

    roll_var = tk.StringVar()

    ttk.Label(frame, text="Enter Roll Number").pack()
    ttk.Entry(frame, textvariable=roll_var).pack(pady=5)

    result_lbl = tk.Label(frame, font=("Arial", 10))
    result_lbl.pack(pady=10)

    def search():
        cursor.execute(
            "SELECT roll_no, name, age, course, phone, email FROM students WHERE roll_no=%s",
            (roll_var.get(),)
        )
        row = cursor.fetchone()
        if row:
            result_lbl.config(
                text=f"Roll: {row[0]}\nName: {row[1]}\nAge: {row[2]}\nCourse: {row[3]}\nPhone: {row[4]}\nEmail: {row[5]}",
                fg="green"
            )
        else:
            result_lbl.config(text="Student not found!", fg="red")

    ttk.Button(frame, text="Search", command=search).pack(pady=5)
    ttk.Button(frame, text="Back", command=lambda: Submit("admin")).pack()

def delete_student():
    clear_screen()

    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    tk.Label(frame, text="❌ Delete Student", font=("Arial", 14, "bold")).pack(pady=10)

    roll_var = tk.StringVar()

    ttk.Label(frame, text="Enter Roll Number").pack()
    ttk.Entry(frame, textvariable=roll_var).pack(pady=5)

    def delete():
        if not roll_var.get():
            messagebox.showerror("Error", "Roll number required")
            return

        confirm = messagebox.askyesno(
            "Confirm",
            "Are you sure you want to delete this student?"
        )
        if confirm:
            cursor.execute("DELETE FROM students WHERE roll_no=%s", (roll_var.get(),))
            conn.commit()
            messagebox.showinfo("Success", "Student deleted successfully")

    ttk.Button(frame, text="Delete", command=delete).pack(pady=5)
    ttk.Button(frame, text="Back", command=lambda: Submit("admin")).pack()


def Submit(passwd):
    if passwd == "admin":
        clear_screen()

        admin = tk.Frame(root)
        admin.pack(fill="both", expand=True, padx=30, pady=20)

        tk.Label(
            admin, text="• 👑 welcome Administrator •",
            font=("Arial", 16, "bold"),
            bg="darkblue", fg="white",
            pady=12
        ).pack(fill="x", pady=(0, 20))

        # BUTTON CONTAINER
        btn_frame = tk.Frame(admin)
        btn_frame.pack()

        btn_frame.columnconfigure(0, weight=1)
        btn_frame.columnconfigure(1, weight=1)

        # ROW 1
        ttk.Button(
            btn_frame, text="👀 Show All Students",
            command=show_all_students, padding=10
        ).grid(row=0, column=0, padx=10, pady=8, sticky="ew")

        ttk.Button(
            btn_frame, text="➕ Add Student",
            command=add_std, padding=10
        ).grid(row=0, column=1, padx=10, pady=8, sticky="ew")

        # ROW 2
        ttk.Button(
            btn_frame, text="✏️ Update Student",
            command=update_student, padding=10
        ).grid(row=1, column=0, padx=10, pady=8, sticky="ew")

        ttk.Button(
            btn_frame, text="❌ Delete Student",
            command=delete_student, padding=10
        ).grid(row=1, column=1, padx=10, pady=8, sticky="ew")

        # ROW 3
        ttk.Button(
            btn_frame, text="🔍 Search Student",
            command=search_student, padding=10
        ).grid(row=2, column=0, padx=10, pady=8, sticky="ew")

        ttk.Button(
            btn_frame, text="📤 Export Data",
            command=export_students, padding=10
        ).grid(row=2, column=1, padx=10, pady=8, sticky="ew")

        # ROW 4
        ttk.Button(
            btn_frame, text="🔑 Change Admin Password",
            command=change_admin_password, padding=10
        ).grid(row=3, column=0, padx=10, pady=8, sticky="ew")

        ttk.Button(
            btn_frame, text="🏠 Home",
            command=main_screen, padding=10
        ).grid(row=3, column=1, padx=10, pady=8, sticky="ew")

    else:
        messagebox.showerror(
            title="Error!",
            message="Wrong Administrator Password!"
        )

        

# ---------- MAIN SCREEN ----------
def main_screen():
    clear_screen()

    tk.Label(
        root, text="• You are a •",
        font=("Arial", 15, "bold"),
        bg="darkblue", fg="white",
        pady=10
    ).pack(fill="x")

    ttk.Button(root, text="Login as Student", command=student).pack(pady=15)
    ttk.Button(root, text="Login as Administrator", command=administrator).pack()

# ---------- START ----------
main_screen()
root.mainloop()
conn.close()