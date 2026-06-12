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
    confirm = messagebox.askyesno("Logout", "Are you sure?")
    if confirm:
        window.destroy()
        import sys
        sys.exit()

def open_login():

    login_win = tk.Toplevel(window)
    login_win.title("Login")
    login_win.geometry("650x500")
    login_win.configure(bg="white")

    frame = tk.Frame(login_win, bg="white")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(
        frame,
        text="LOGIN",
        font=("Arial", 36, "bold"),
        fg="#800000",
        bg="white"
    ).pack(pady=20)

    tk.Label(frame, text="USERNAME", bg="white", font=("Arial", 14)).pack()

    username_entry = tk.Entry(
        frame,
        font=("Arial", 16),
        width=30,
        justify="center"
    )
    username_entry.pack(pady=10)

    tk.Label(frame, text="PASSWORD", bg="white", font=("Arial", 14)).pack()

    password_entry = tk.Entry(
        frame,
        font=("Arial", 16),
        width=30,
        show="*",
        justify="center"
    )
    password_entry.pack(pady=10)

    def do_login():
        username = username_entry.get()
        password = password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Fill all fields")
            return

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
        font=("Arial", 16, "bold"),
        width=20,
        bg="#800000",
        fg="white",
        command=do_login
    ).pack(pady=25)

def open_register():

    reg_win = tk.Toplevel(window)
    reg_win.title("Register")
    reg_win.geometry("600x500")
    reg_win.configure(bg="white")

    frame = tk.Frame(reg_win, bg="white")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="REGISTER",
             font=("Arial", 34, "bold"),
             fg="#800000", bg="white").pack(pady=10)

    tk.Label(frame, text="USERNAME", bg="white").pack()
    username_entry = tk.Entry(frame, font=("Arial", 16), width=30, justify="center")
    username_entry.pack(pady=8)

    tk.Label(frame, text="PASSWORD", bg="white").pack()
    password_entry = tk.Entry(frame, font=("Arial", 16), width=30, show="*", justify="center")
    password_entry.pack(pady=8)

    tk.Label(frame, text="ROLE (admin/user)", bg="white").pack()
    role_entry = tk.Entry(frame, font=("Arial", 16), width=30, justify="center")
    role_entry.pack(pady=8)

    def do_register():
        username = username_entry.get()
        password = password_entry.get()
        role = role_entry.get().lower()

        if not username or not password:
            messagebox.showerror("Error", "All fields required")
            return

        if role not in ["admin", "user"]:
            role = "user"

        with open("accounts.txt", "a") as f:
            f.write(f"{username},{password},{role}\n")

        messagebox.showinfo("Success", "Account Created!")
        reg_win.destroy()

    tk.Button(
        frame,
        text="REGISTER",
        font=("Arial", 16, "bold"),
        width=20,
        bg="#FFD700",
        fg="black",
        command=do_register
    ).pack(pady=20)

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

def open_edit_student(selected_data):

    edit_win = tk.Toplevel(window)
    edit_win.title("Edit Student")
    edit_win.geometry("400x400")
    edit_win.configure(bg="white")

    tk.Label(
        edit_win,
        text="EDIT STUDENT",
        font=("Arial", 18, "bold"),
        fg="#800000",
        bg="white"
    ).pack(pady=10)

    sid, name, age, course, grade = selected_data

    tk.Label(edit_win, text="Name", bg="white").pack()
    name_entry = tk.Entry(edit_win)
    name_entry.insert(0, name)
    name_entry.pack()

    tk.Label(edit_win, text="Age", bg="white").pack()
    age_entry = tk.Entry(edit_win)
    age_entry.insert(0, age)
    age_entry.pack()

    tk.Label(edit_win, text="Course", bg="white").pack()
    course_entry = tk.Entry(edit_win)
    course_entry.insert(0, course)
    course_entry.pack()

    tk.Label(edit_win, text="Grade", bg="white").pack()
    grade_entry = tk.Entry(edit_win)
    grade_entry.insert(0, grade)
    grade_entry.pack()

    def save_edit():
        try:
            with open("students.txt", "r") as f:
                lines = f.readlines()

            with open("students.txt", "w") as f:
                for line in lines:
                    data = line.strip().split(",")

                    if data[0] == sid:
                        f.write(f"{sid},{name_entry.get()},{age_entry.get()},{course_entry.get()},{grade_entry.get()}\n")
                    else:
                        f.write(line)
                        
            if not messagebox.askyesno("Confirm", "Update this student record?"):
             return
            
            messagebox.showinfo("Success", "Student updated!")
            edit_win.destroy()

        except FileNotFoundError:
            messagebox.showerror("Error", "File not found")

    tk.Button(
        edit_win,
        text="SAVE",
        bg="#800000",
        fg="white",
        command=save_edit
    ).pack(pady=10)

def open_update_student():

    up_win = tk.Toplevel(window)
    up_win.title("Update Student")
    up_win.geometry("600x500")
    up_win.configure(bg="white")

    frame = tk.Frame(up_win, bg="white")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(
        frame,
        text="UPDATE STUDENT",
        font=("Arial", 24, "bold"),
        fg="#800000",
        bg="white"
    ).pack(pady=10)

    tk.Label(frame, text="Enter Student ID", bg="white").pack()
    id_entry = tk.Entry(frame, font=("Arial", 14), width=30, justify="center")
    id_entry.pack(pady=10)

    # fields
    name_entry = tk.Entry(frame, font=("Arial", 14), width=30, justify="center")
    age_entry = tk.Entry(frame, font=("Arial", 14), width=30, justify="center")
    course_entry = tk.Entry(frame, font=("Arial", 14), width=30, justify="center")
    grade_entry = tk.Entry(frame, font=("Arial", 14), width=30, justify="center")

    def load_student():

        sid = id_entry.get()

        try:
            with open("students.txt", "r") as f:
                lines = f.readlines()

            for line in lines:
                data = line.strip().split(",")

                if data[0] == sid:
                    name_entry.delete(0, "end")
                    age_entry.delete(0, "end")
                    course_entry.delete(0, "end")
                    grade_entry.delete(0, "end")

                    name_entry.insert(0, data[1])
                    age_entry.insert(0, data[2])
                    course_entry.insert(0, data[3])
                    grade_entry.insert(0, data[4])

                    messagebox.showinfo("Found", "Student loaded!")
                    return

            messagebox.showerror("Error", "Student not found")

        except FileNotFoundError:
            messagebox.showerror("Error", "No file found")

    tk.Button(frame, text="LOAD", command=load_student,
              bg="#800000", fg="white").pack(pady=5)

    tk.Label(frame, text="NAME", bg="white").pack()
    name_entry.pack(pady=5)

    tk.Label(frame, text="AGE", bg="white").pack()
    age_entry.pack(pady=5)

    tk.Label(frame, text="COURSE", bg="white").pack()
    course_entry.pack(pady=5)

    tk.Label(frame, text="GRADE", bg="white").pack()
    grade_entry.pack(pady=5)

def open_search_student():

    search_win = tk.Toplevel(window)
    search_win.title("Search Student")
    search_win.geometry("600x400")
    search_win.configure(bg="white")

    frame = tk.Frame(search_win, bg="white")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame,
             text="SEARCH STUDENT",
             font=("Arial", 24, "bold"),
             fg="#800000",
             bg="white").pack(pady=10)

    tk.Label(frame, text="Enter Name", bg="white").pack()

    name_entry = tk.Entry(frame, font=("Arial", 14), width=30, justify="center")
    name_entry.pack(pady=10)

    result_box = tk.Text(frame, font=("Arial", 12), width=60, height=10)
    result_box.pack(pady=10)

    def do_search():

        keyword = name_entry.get().lower()
        result_box.delete("1.0", "end")

        found = False

        try:
            with open("students.txt", "r") as f:
                for line in f:
                    if keyword in line.lower():
                        result_box.insert("end", line)
                        found = True

            if not found:
                result_box.insert("end", "No student found.")

        except FileNotFoundError:
            result_box.insert("end", "No file found.")

    tk.Button(
        frame,
        text="SEARCH",
        font=("Arial", 14, "bold"),
        bg="#800000",
        fg="white",
        width=15,
        command=do_search
    ).pack(pady=10)

def open_delete_student():

    del_win = tk.Toplevel(window)
    del_win.title("Delete Student")
    del_win.geometry("600x400")
    del_win.configure(bg="white")

    frame = tk.Frame(del_win, bg="white")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(
        frame,
        text="DELETE STUDENT",
        font=("Arial", 24, "bold"),
        fg="#800000",
        bg="white"
    ).pack(pady=10)

    tk.Label(frame, text="Enter Student ID", bg="white", font=("Arial", 12)).pack()

    id_entry = tk.Entry(frame, font=("Arial", 14), width=30, justify="center")
    id_entry.pack(pady=10)

    def do_delete():

        sid = id_entry.get()
        if not sid:
            return

        try:
            with open("students.txt", "r") as f:
                lines = f.readlines()

            found = False
            new_lines = []

            for line in lines:
                if line.split(",")[0] != sid:
                    new_lines.append(line)
                else:
                    found = True

            if not found:
                messagebox.showerror("Error", "Student not found")
                return

            confirm = messagebox.askyesno("Confirm", "Delete this student?")

            if confirm:
                with open("students.txt", "w") as f:
                    f.writelines(new_lines)

                messagebox.showinfo("Success", "Student deleted!")
                del_win.destroy()

        except FileNotFoundError:
            messagebox.showerror("Error", "No file found")

    tk.Button(
        frame,
        text="DELETE",
        font=("Arial", 14, "bold"),
        bg="#800000",
        fg="white",
        width=15,
        command=do_delete
    ).pack(pady=10)

def open_statistics():

    stat_win = tk.Toplevel(window)
    stat_win.title("Statistics")
    stat_win.geometry("700x500")
    stat_win.configure(bg="white")

    frame = tk.Frame(stat_win, bg="white")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(
        frame,
        text="STUDENT STATISTICS",
        font=("Arial", 24, "bold"),
        fg="#800000",
        bg="white"
    ).pack(pady=10)

    text_box = tk.Text(frame, font=("Arial", 12), width=60, height=20)
    text_box.pack(pady=10)

    try:
        with open("students.txt", "r") as f:
            lines = f.readlines()

        if not lines:
            text_box.insert("end", "No student records found.")
            return

        total = len(lines)

        grades = []
        passed = 0
        failed = 0

        for line in lines:
            data = line.strip().split(",")
            grade = float(data[4])
            grades.append(grade)

            if grade >= 75:
                passed += 1
            else:
                failed += 1

        avg = sum(grades) / total
        highest = max(grades)
        lowest = min(grades)

        text_box.insert("end", f"Total Students: {total}\n")
        text_box.insert("end", f"Passed: {passed}\n")
        text_box.insert("end", f"Failed: {failed}\n\n")
        text_box.insert("end", f"Average Grade: {avg:.2f}\n")
        text_box.insert("end", f"Highest Grade: {highest}\n")
        text_box.insert("end", f"Lowest Grade: {lowest}\n")

    except FileNotFoundError:
        text_box.insert("end", "No file found.")

def open_change_password():

    win = tk.Toplevel(window)
    win.title("Change Password")
    win.geometry("400x300")

    tk.Label(win, text="Change Password", font=("Arial", 16, "bold")).pack(pady=10)

    old_pass = tk.Entry(win, show="*")
    old_pass.pack(pady=5)

    new_pass = tk.Entry(win, show="*")
    new_pass.pack(pady=5)

    def update_pass():
        user = current_user["username"]

        try:
            with open("accounts.txt", "r") as f:
                lines = f.readlines()

            with open("accounts.txt", "w") as f:
                for line in lines:
                    u, p, r = line.strip().split(",")

                    if u == user and p == old_pass.get():
                        f.write(f"{u},{new_pass.get()},{r}\n")
                    else:
                        f.write(line)

            messagebox.showinfo("Success", "Password updated!")
            win.destroy()

        except:
            messagebox.showerror("Error", "Something went wrong")

    tk.Button(win, text="UPDATE", command=update_pass,
              bg="#800000", fg="white").pack(pady=10)

    def save_update():
        sid = id_entry.get()

        try:
            with open("students.txt", "r") as f:
                lines = f.readlines()

            new_lines = []

            for line in lines:
                data = line.strip().split(",")

                if data[0] == sid:
                    new_line = f"{sid},{name_entry.get()},{age_entry.get()},{course_entry.get()},{grade_entry.get()}\n"
                    new_lines.append(new_line)
                else:
                    new_lines.append(line)

            with open("students.txt", "w") as f:
                f.writelines(new_lines)

            messagebox.showinfo("Success", "Student updated!")
            up_win.destroy()

        except FileNotFoundError:
            messagebox.showerror("Error", "No file found")

    tk.Button(
        frame,
        text="SAVE UPDATE",
        font=("Arial", 14, "bold"),
        bg="#800000",
        fg="white",
        width=15,
        command=save_update
    ).pack(pady=10)

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
).grid(row=0, column=0, padx=15, pady=10)

tk.Button(
    button_frame,
    text="REGISTER",
    font=("Arial", 16, "bold"),
    width=15,
    height=2,
    bg="#FFD700",
    fg="black",
    command=open_register
).grid(row=0, column=1, padx=15, pady=10)

tk.Button(
    button_frame,
    text="EXIT",
    font=("Arial", 16, "bold"),
    width=15,
    height=2,
    bg="red",
    fg="white",
    command=window.destroy
).grid(row=0, column=2, padx=15, pady=10)

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