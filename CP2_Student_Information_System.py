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

def add_student():
    if len(names) >= MAX_STUDENTS:
        print("\n  [!] Student limit reached.")
        return

    print_header("ADD STUDENT")

    name = prompt_non_empty("  Name    : ")
    age = int(prompt_positive_number("  Age     : "))
    course = prompt_non_empty("  Course  : ")
    grade = prompt_positive_number("  Grade   : ")

    names.append(name)
    ages.append(age)
    courses.append(course)
    grades.append(grade)

    print("\n  [✓] Student added successfully!")

def view_students():
    print_header("STUDENT RECORDS")

    if len(names) == 0:
        print("  No student records yet.")
        return

    print(f"  {'No.':<4} {'Name':<18} {'Age':<5} {'Course':<12} {'Grade':<8}")
    print_divider(60)

    for i in range(len(names)):
        print(f"  {i+1:<4} {names[i]:<18} {ages[i]:<5} {courses[i]:<12} {grades[i]:<8.2f}")

    print_divider(60)
    print(f"  Total students: {len(names)}")

def update_student():
    view_students()
    if len(names) == 0:
        return

    index = int(prompt_positive_number("  Enter student number to update: ")) - 1

    if 0 <= index < len(names):
        print("\n  Enter new details:")

        names[index] = prompt_non_empty("  Name    : ")
        ages[index] = int(prompt_positive_number("  Age     : "))
        courses[index] = prompt_non_empty("  Course  : ")
        grades[index] = prompt_positive_number("  Grade   : ")

        print("\n  [✓] Student updated!")
    else:
        print("  [!] Invalid selection.")

        # add delete student