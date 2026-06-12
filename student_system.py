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