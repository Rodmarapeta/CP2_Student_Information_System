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

def prompt_age(prompt):
    while True:
        try:
            age = int(input(prompt))
            if 0 <= age <= 100:
                return age
            print("  [!] Age must be between 0 and 100.")
        except:
            print("  [!] Invalid input.")

def prompt_grade(prompt):
    while True:
        try:
            grade = float(input(prompt))
            if 0 <= grade <= 100:
                return grade
            print("  [!] Grade must be between 0 and 100.")
        except:
            print("  [!] Invalid input.")

def show_menu():
    print("\n+----------------------------------+")
    print("|  STUDENT INFORMATION SYSTEM     |")
    print("+----------------------------------+")
    print("|  1. Add Student                 |")
    print("|  2. View Students               |")
    print("|  3. Update Student              |")
    print("|  4. Delete Student              |")
    print("|  5. Search Student              |")
    print("|  6. Sort Students               |")
    print("|  7. Statistics                  |")
    print("|  8. Exit                        |")
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

def sort_students(names, ages, courses, grades, ids):
    combined = list(zip(ids, names, ages, courses, grades))
    combined.sort(key=lambda x: x[1])  

    ids[:], names[:], ages[:], courses[:], grades[:] = zip(*combined)
    save_data(names, ages, courses, grades, ids)
    print("  [✓] Sorted by name!")

def statistics(names, courses, grades):
    print_header("STUDENT STATISTICS")

    if len(names) == 0:
        print("  No student records available.")
        return

    total_students = len(names)

    average_grade = sum(grades) / total_students

    highest_grade = max(grades)
    lowest_grade = min(grades)

    highest_student = names[grades.index(highest_grade)]
    lowest_student = names[grades.index(lowest_grade)]

    passed = 0
    failed = 0

    for grade in grades:
        if grade >= 75:
            passed += 1
        else:
            failed += 1

    print(f"\n  Total Students  : {total_students}")
    print(f"  Passed Students : {passed}")
    print(f"  Failed Students : {failed}")
    print(f"  Average Grade   : {average_grade:.2f}")
    print(f"  Highest Grade   : {highest_grade:.2f} ({highest_student})")
    print(f"  Lowest Grade    : {lowest_grade:.2f} ({lowest_student})")

    print("\n  AVERAGE GRADE PER COURSE")
    print_divider(35)

    unique_courses = []

    for course in courses:
        if course not in unique_courses:
            unique_courses.append(course)

    for course in unique_courses:
        total = 0
        count = 0

        for i in range(len(courses)):
            if courses[i] == course:
                total += grades[i]
                count += 1

        average = total / count
        print(f"  {course:<15} : {average:.2f}")

    print("\n  TOP 3 STUDENTS")
    print_divider(35)

    students = []

    for i in range(len(names)):
        students.append((names[i], courses[i], grades[i]))

    students.sort(key=lambda x: x[2], reverse=True)

    top_count = min(3, len(students))

    for i in range(top_count):
        print(
            f"  {i+1}. {students[i][0]} "
            f"({students[i][1]}) - {students[i][2]:.2f}"
        )

        ACCOUNT_FILE = "accounts.txt"

def register():
    print_header("REGISTER")

    username = input("Create Username: ")
    password = input("Create Password: ")

    role = input("Role (admin/user): ").lower()

    if role not in ["admin", "user"]:
        role = "user"

    with open(ACCOUNT_FILE, "a") as file:
        file.write(f"{username},{password},{role}\n")

    print("\n  [✓] Account created successfully!")
    
def login():
    print_header("LOGIN")

    while True:

        username = input("Username: ")
        password = input("Password: ")

        try:
            with open(ACCOUNT_FILE, "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if len(data) == 3:

                        user, pwd, role = data

                        if username == user and password == pwd:
                            print("\n  [✓] Login Successful!")
                            return username, role

            print("\n  [!] Invalid username or password.")

        except FileNotFoundError:
            print("No account found.")
            register()def login():
    print_header("LOGIN")

    while True:

        username = input("Username: ")
        password = input("Password: ")

        try:
            with open(ACCOUNT_FILE, "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if len(data) == 3:

                        user, pwd, role = data

                        if username == user and password == pwd:
                            print("\n  [✓] Login Successful!")
                            return username, role

            print("\n  [!] Invalid username or password.")

        except FileNotFoundError:
            print("No account found.")
            register()
            
