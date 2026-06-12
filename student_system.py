import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

current_user = {"username": None, "role": None}

window = tk.Tk()
window.title("Student Information System")
window.geometry("1200x700")
window.configure(bg="white")

def exit_app():
    confirm = messagebox.askyesno("Exit", "Are you sure you want to exit?")
    if confirm:
        window.destroy()

def logout():
    confirm = messagebox.askyesno("Logout", "Are you sure you want to logout?")
    if confirm:
        window.destroy()
        import os
        os.system("python gui.py")

def open_login(): 

    login_win = tk.Toplevel(window)
    login_win.title("Login")
    login_win.geometry("450x350")
    login_win.configure(bg="white")

    frame = tk.Frame(login_win, bg="white")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="LOGIN",
             font=("Arial", 34, "bold"),
             fg="#800000", bg="white").pack(pady=10)

    tk.Label(frame, text="USERNAME", font=("Arial", 14, "bold"), bg="white").pack()
    username_entry = tk.Entry(frame, font=("Arial", 14), width=25, justify="center")
    username_entry.pack(pady=5)

    tk.Label(frame, text="PASSWORD", font=("Arial", 14, "bold"), bg="white").pack()
    password_entry = tk.Entry(frame, font=("Arial", 14), width=25, show="*", justify="center")
    password_entry.pack(pady=5)

    def do_login():
        username = username_entry.get()
        password = password_entry.get()

        try:
            with open("accounts.txt", "r") as f:
                for line in f:
                    user, pwd, role = line.strip().split(",")

                    if username == user and password == pwd:

                        current_user["username"] = user
                        current_user["role"] = role

                        messagebox.showinfo(
                            "Success",
                            f"Login Successful!\nRole: {role}"
                        )

                        login_win.destroy()
                        open_dashboard()
                        return

            messagebox.showerror("Error", "Invalid login")

        except FileNotFoundError:
            messagebox.showerror("Error", "No accounts found")

    tk.Button(
        frame,
        text="LOGIN",
        font=("Arial", 14, "bold"),
        width=18,
        bg="#800000",
        fg="white",
        command=do_login
    ).pack(pady=15)

def open_register():

    reg_win = tk.Toplevel(window)
    reg_win.title("Register")
    reg_win.geometry("500x400")
    reg_win.configure(bg="white")

    frame = tk.Frame(reg_win, bg="white")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="REGISTER", font=("Arial", 34, "bold"),
             fg="#800000", bg="white").pack(pady=10)

    tk.Label(frame, text="USERNAME", font=("Arial", 14, "bold"), bg="white").pack()
    username_entry = tk.Entry(frame, font=("Arial", 14), width=25, justify="center")
    username_entry.pack(pady=5)

    tk.Label(frame, text="PASSWORD", font=("Arial", 14, "bold"), bg="white").pack()
    password_entry = tk.Entry(frame, font=("Arial", 14), width=25, show="*", justify="center")
    password_entry.pack(pady=5)

    tk.Label(frame, text="ROLE (admin/user)", font=("Arial", 14, "bold"), bg="white").pack()
    role_entry = tk.Entry(frame, font=("Arial", 14), width=25, justify="center")
    role_entry.pack(pady=5)

    def do_register():
        username = username_entry.get()
        password = password_entry.get()
        role = role_entry.get().lower()

        if role not in ["admin", "user"]:
            role = "user"

        with open("accounts.txt", "a") as f:
            f.write(f"{username},{password},{role}\n")

        messagebox.showinfo("Success", "Account Created!")
        reg_win.destroy()

    tk.Button(
        frame,
        text="REGISTER",
        font=("Arial", 14, "bold"),
        width=18,
        bg="#FFD700",
        fg="black",
        command=do_register
    ).pack(pady=15)

def open_add_student():

    add_win = tk.Toplevel(window)
    add_win.title("Add Student")
    add_win.geometry("500x450")
    add_win.configure(bg="white")

    frame = tk.Frame(add_win, bg="white")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="ADD STUDENT",
             font=("Arial", 28, "bold"),
             fg="#800000", bg="white").pack(pady=10)

    tk.Label(frame, text="ID", bg="white").pack()
    id_entry = tk.Entry(frame, font=("Arial", 14), width=25, justify="center")
    id_entry.pack(pady=5)

    tk.Label(frame, text="NAME", bg="white").pack()
    name_entry = tk.Entry(frame, font=("Arial", 14), width=25, justify="center")
    name_entry.pack(pady=5)

    tk.Label(frame, text="AGE", bg="white").pack()
    age_entry = tk.Entry(frame, font=("Arial", 14), width=25, justify="center")
    age_entry.pack(pady=5)

    tk.Label(frame, text="COURSE", bg="white").pack()
    course_entry = tk.Entry(frame, font=("Arial", 14), width=25, justify="center")
    course_entry.pack(pady=5)

    tk.Label(frame, text="GRADE", bg="white").pack()
    grade_entry = tk.Entry(frame, font=("Arial", 14), width=25, justify="center")
    grade_entry.pack(pady=5)

    def save_student():
     sid = id_entry.get().strip()
    name = name_entry.get().strip()
    age = age_entry.get().strip()
    course = course_entry.get().strip()
    grade = grade_entry.get().strip()

    if not sid or not name or not age or not course or not grade:
        messagebox.showerror("Error", "Fill all fields!")
        return

    if not age.isdigit():
        messagebox.showerror("Error", "Age must be a number")
        return

    try:
        grade_num = float(grade)

        if grade_num < 0 or grade_num > 100:
            messagebox.showerror(
                "Error",
                "Grade must be between 0 and 100"
            )
            return

    except ValueError:
        messagebox.showerror(
            "Error",
            "Grade must be numeric"
        )
        return

    try:
        with open("students.txt", "r") as f:
            for line in f:
                if line.strip().split(",")[0] == sid:
                    messagebox.showerror(
                        "Error",
                        "Student ID already exists!"
                    )
                    return
    except FileNotFoundError:
        pass

    confirm = messagebox.askyesno(
        "Confirm Save",
        "Are you sure you want to save this student?"
    )

    if not confirm:
        return

    with open("students.txt", "a") as f:
        f.write(f"{sid},{name},{age},{course},{grade}\n")

    messagebox.showinfo(
        "Success",
        "Student Added Successfully!"
    )

    add_win.destroy()

    tk.Button(
        frame,
        text="SAVE",
        font=("Arial", 14, "bold"),
        width=18,
        bg="#800000",
        fg="white",
        command=save_student
    ).pack(pady=15)

def open_view_students():

    view_win = tk.Toplevel(window)
    view_win.title("View Students")
    view_win.geometry("900x550")

    frame = tk.Frame(view_win)
    frame.pack(fill="both", expand=True)

    tk.Label(frame, text="STUDENT RECORDS",
             font=("Arial", 18, "bold")).pack()

    columns = ("ID", "Name", "Age", "Course", "Grade")

    tree = ttk.Treeview(frame, columns=columns, show="headings")
    tree.pack(fill="both", expand=True)

    for col in columns:
        tree.heading(col, text=col)

    def load_data():
        tree.delete(*tree.get_children())
        try:
            with open("students.txt", "r") as f:
                for line in f:
                    tree.insert("", "end", values=line.strip().split(","))
        except FileNotFoundError:
            messagebox.showerror("Error", "No file found")

    def sort_by_id(desc=False):
        data = [tree.item(i)["values"] for i in tree.get_children()]

        # convert ID safely to int
        data.sort(key=lambda x: int(x[0]), reverse=desc)

        tree.delete(*tree.get_children())
        for row in data:
            tree.insert("", "end", values=row)

    def sort_by_grade(desc=True):
        data = [tree.item(i)["values"] for i in tree.get_children()]
        data.sort(key=lambda x: float(x[4]), reverse=desc)

        tree.delete(*tree.get_children())
        for row in data:
            tree.insert("", "end", values=row)

    def sort_by_name():
        data = [tree.item(i)["values"] for i in tree.get_children()]
        data.sort(key=lambda x: x[1].lower())

        tree.delete(*tree.get_children())
        for row in data:
            tree.insert("", "end", values=row)

    load_data()

    btn_frame = tk.Frame(frame)
    btn_frame.pack()

    tk.Button(btn_frame, text="Grade High → Low",
              command=lambda: sort_by_grade(True)).pack(side="left")

    tk.Button(btn_frame, text="Grade Low → High",
              command=lambda: sort_by_grade(False)).pack(side="left")

    tk.Button(btn_frame, text="Sort A → Z",
              command=sort_by_name).pack(side="left")

    tk.Button(btn_frame, text="ID Low → High",
              command=lambda: sort_by_id(False)).pack(side="left")

    tk.Button(btn_frame, text="ID High → Low",
              command=lambda: sort_by_id(True)).pack(side="left")

    def on_select(event):
        selected = tree.focus()
        if selected:
            values = tree.item(selected, "values")
            open_edit_student(values)

    tree.bind("<Double-1>", on_select)

def open_dashboard():

    dash = tk.Toplevel(window)
    dash.title("Dashboard")
    dash.geometry("1000x600")
    dash.configure(bg="white")

    frame = tk.Frame(dash, bg="white")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(
        frame,
        text="STUDENT INFORMATION SYSTEM",
        font=("Arial", 30, "bold"),
        fg="#800000",
        bg="white"
    ).pack(pady=20)

    btn_frame = tk.Frame(frame, bg="white")
    btn_frame.pack(pady=20)

    role = current_user["role"]

    if role == "admin":

        tk.Button(btn_frame, text="ADD STUDENT", width=20,
                  bg="#800000", fg="white",
                  command=open_add_student).grid(row=0, column=0, padx=10, pady=10)

        tk.Button(btn_frame, text="VIEW STUDENTS", width=20,
                  bg="#800000", fg="white",
                  command=open_view_students).grid(row=0, column=1, padx=10, pady=10)

        tk.Button(btn_frame, text="SEARCH", width=20,
                  bg="#800000", fg="white",
                  command=open_search_student).grid(row=1, column=0, padx=10, pady=10)

        tk.Button(btn_frame, text="STATISTICS", width=20,
                  bg="#800000", fg="white",
                  command=open_statistics).grid(row=1, column=1, padx=10, pady=10)

        tk.Button(btn_frame, text="UPDATE STUDENT", width=20,
                  bg="#800000", fg="white",
                  command=open_update_student).grid(row=2, column=0, padx=10, pady=10)

        tk.Button(btn_frame, text="DELETE STUDENT", width=20,
                  bg="#800000", fg="white",
                  command=open_delete_student).grid(row=2, column=1, padx=10, pady=10)

        tk.Button(btn_frame, text="CHANGE PASSWORD", width=20,
                  bg="#800000", fg="white",
                  command=open_change_password).grid(row=3, column=0, padx=10, pady=10)

        tk.Button(btn_frame, text="LOGOUT", width=20,
                  bg="orange", fg="white",
                  command=logout).grid(row=3, column=1, padx=10, pady=10)

    else:

        tk.Button(btn_frame, text="VIEW STUDENTS", width=20,
                  bg="#800000", fg="white",
                  command=open_view_students).grid(row=0, column=0, padx=10, pady=10)

        tk.Button(btn_frame, text="SEARCH", width=20,
                  bg="#800000", fg="white",
                  command=open_search_student).grid(row=0, column=1, padx=10, pady=10)

        tk.Button(btn_frame, text="STATISTICS", width=20,
                  bg="#800000", fg="white",
                  command=open_statistics).grid(row=1, column=0, padx=10, pady=10)

        tk.Button(btn_frame, text="CHANGE PASSWORD", width=20,
                  bg="#800000", fg="white",
                  command=open_change_password).grid(row=1, column=1, padx=10, pady=10)

        tk.Button(btn_frame, text="LOGOUT", width=20,
                  bg="orange", fg="white",
                  command=logout).grid(row=2, column=0, padx=10, pady=10)

        tk.Button(frame, text="EXIT APP",
                  bg="red", fg="white",
                  command=exit_app).pack(pady=10)


frame = tk.Frame(window, bg="white")
frame.place(relx=0.5, rely=0.45, anchor="center")

title = tk.Label(
    frame,
    text="STUDENT INFORMATION SYSTEM",
    font=("Arial", 42, "bold"),
    fg="#800000",
    bg="white"
)
title.pack(pady=40)

button_frame = tk.Frame(frame, bg="white")
button_frame.pack(pady=70)

tk.Button(
    button_frame,
    text="LOGIN",
    font=("Arial", 16, "bold"),
    width=15,
    height=2,
    bg="#800000",
    fg="white",
    command=open_login
).grid(row=0, column=0, padx=15)

tk.Button(
    button_frame,
    text="REGISTER",
    font=("Arial", 16, "bold"),
    width=15,
    height=2,
    bg="#FFD700",
    fg="black",
    command=open_register
).grid(row=0, column=1, padx=15)

tk.Button(
    button_frame,
    text="EXIT",
    font=("Arial", 16, "bold"),
    width=15,
    height=2,
    bg="red",
    fg="white",
    command=window.destroy
).grid(row=0, column=2, padx=15)

tk.Button(button_frame,
    text="CHANGE PASSWORD",
    width=20,
    bg="#800000",
    fg="white",
    command=open_change_password
).grid(row=3, column=0)

tk.Button(button_frame,
    text="LOGOUT",
    width=20,
    bg="orange",
    fg="white",
    command=logout
).grid(row=3, column=1)

window.mainloop()

