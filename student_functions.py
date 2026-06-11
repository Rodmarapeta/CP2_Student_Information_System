from file_handler import save_data

MAX_STUDENTS = 100

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

def add_student(names, ages, courses, grades, ids):
    if len(names) >= MAX_STUDENTS:
        print("\n  [!] Student limit reached.")
        return

    print_header("ADD STUDENT")

    name = prompt_non_empty("  Name    : ")
    
    if name in names:
        print("  [!] Student already exists.")
        return

    age = prompt_age("  Age     : ")
    course = prompt_non_empty("  Course  : ")
    grade = prompt_grade("  Grade   : ")

    new_id = ids[-1] + 1 if ids else 1

    ids.append(new_id)
    names.append(name)
    ages.append(age)
    courses.append(course)
    grades.append(grade)

    save_data(names, ages, courses, grades, ids)
    print("\n  [✓] Student added successfully!")

def view_students(names, ages, courses, grades, ids):
    print_header("STUDENT RECORDS")

    if len(names) == 0:
        print("  No student records yet.")
        return

    print(f"{'ID':<5}{'Name':<18}{'Age':<5}{'Course':<12}{'Grade':<8}")
    print_divider(55)

    for i in range(len(names)):
        print(f"{ids[i]:<5}{names[i]:<18}{ages[i]:<5}{courses[i]:<12}{grades[i]:<8.2f}")

def update_student(names, ages, courses, grades, ids):
    if len(names) == 0:
        return

    try:
        id_input = int(input("Enter ID to update: "))

        if id_input in ids:
            index = ids.index(id_input)

            print("\nEnter new details:")
            names[index] = prompt_non_empty("Name: ")
            ages[index] = prompt_age("Age: ")
            courses[index] = prompt_non_empty("Course: ")
            grades[index] = prompt_grade("Grade: ")

            save_data(names, ages, courses, grades, ids)
            print("\n  [✓] Student updated!")

        else:
            print("  [!] ID not found.")

    except:
        print("  [!] Invalid input.")

def delete_student(names, ages, courses, grades, ids):
    try:
        id_input = int(input("Enter ID to delete: "))

        if id_input in ids:
            index = ids.index(id_input)

            confirm = input(f"Delete {names[index]}? (yes/no): ")
            if confirm.lower() == "yes":

                for arr in (names, ages, courses, grades, ids):
                    arr.pop(index)

                save_data(names, ages, courses, grades, ids)
                print("  [✓] Deleted successfully!")

        else:
            print("  [!] ID not found.")

    except:
        print("  [!] Invalid input.")

def search_student(names, ages, courses, grades):
    keyword = input("Enter name: ").lower()
    found = False

    for i in range(len(names)):
        if keyword in names[i].lower():
            print(f"{names[i]} | {courses[i]} | {grades[i]}")
            found = True

    if not found:
        print("No match found.")
