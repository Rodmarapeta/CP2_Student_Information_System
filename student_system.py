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