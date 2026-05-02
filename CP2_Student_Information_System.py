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
    print("\n+----------------------------------+")
    print("|  STUDENT INFORMATION SYSTEM     |")
    print("+----------------------------------+")
    print("|  1. Add Student                 |")
    print("|  2. View Students               |")
    print("|  3. Update Student              |")
    print("|  4. Delete Student              |")
    print("|  5. Search Student              |")
    print("|  6. Exit                        |")
    print("+----------------------------------+")
    print("Choose an option (1-6) ")

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

def delete_student():
    view_students()
    if len(names) == 0:
        return

    index = int(prompt_positive_number("  Enter student number to delete: ")) - 1

    if 0 <= index < len(names):
        names.pop(index)
        ages.pop(index)
        courses.pop(index)
        grades.pop(index)

        print("\n  [✓] Student deleted!")
    else:
        print("  [!] Invalid selection.")

def search_student():
    print_header("SEARCH STUDENT")

    keyword = prompt_non_empty("  Enter name: ").lower()
    found = False

    for i in range(len(names)):
        if keyword in names[i].lower():
            print(f"  Found: {names[i]} | Age: {ages[i]} | Course: {courses[i]} | Grade: {grades[i]:.2f}")
            found = True

    if not found:
        print("  No matching student found.")

def main():
    print_header("STUDENT INFORMATION SYSTEM")

    while True:
        show_menu()
        choice = input("  Enter choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            search_student()
        elif choice == "6":
            print("\n  Thank you for using the system!\n")
            break
        else:
            print("\n  [!] Invalid choice. Enter 1-6.")
            
main()