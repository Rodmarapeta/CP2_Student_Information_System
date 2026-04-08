MAX_STUDENTS = 100

names = []
ages = []
courses = []
grades = []

def print_header(title):
    print("\n  ==============================")
    print(f"  {title}")
    print("  ==============================")

def print_divider(length):
    print("  " + "─" * length)

def prompt_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  [!] This field cannot be empty.")

def prompt_positive_number(prompt):
    while True:
        value = input(prompt).strip()
        try:
            num = float(value)
            if num > 0:
                return num
            print("  [!] Must be greater than 0.")
        except:
            print("  [!] Invalid number.")

def show_menu():
    print("==================================")
    print("|              MENU              |")
    print("==================================")
    print("|  1. Add Student                |")
    print("|  2. View Students              |")
    print("|  3. Update Student             |")
    print("|  4. Delete Student             |")
    print("|  5. Search Student             |")
    print("|  6. Exit                       |")
    print("==================================")

# add student