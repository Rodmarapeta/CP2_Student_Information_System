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