from file_handler import save_data

MAX_STUDENTS = 100
ACCOUNT_FILE = "accounts.txt"


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


def show_menu(role):

    if role == "admin":
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
        print("|  8. Change Password             |")
        print("|  9. Logout                      |")
        print("| 10. Exit                        |")
        print("+----------------------------------+")
    else:
        print("\n+----------------------------------+")
        print("|            USER MENU            |")
        print("+----------------------------------+")
        print("|  1. View Students               |")
        print("|  2. Search Student              |")
        print("|  3. Statistics                  |")
        print("|  4. Change Password             |")
        print("|  5. Logout                      |")
        print("|  6. Exit                        |")
        print("+----------------------------------+")


def add_student(names, ages, courses, grades, ids):

    if len(names) >= MAX_STUDENTS:
        print("\nStudent limit reached.")
        return

    print_header("ADD STUDENT")

    try:
        new_id = int(input("Enter ID: "))

        if new_id in ids:
            print("ID already exists!")
            return

    except:
        print("Invalid ID.")
        return

    name = prompt_non_empty("Name: ")
    age = prompt_age("Age: ")
    course = prompt_non_empty("Course: ")
    grade = prompt_grade("Grade: ")

    ids.append(new_id)
    names.append(name)
    ages.append(age)
    courses.append(course)
    grades.append(grade)

    save_data(names, ages, courses, grades, ids)

    print("\nStudent added successfully!")


def view_students(names, ages, courses, grades, ids):

    if len(names) == 0:
        print("No records.")
        return

    print(f"{'ID':<5}{'Name':<15}{'Age':<5}{'Course':<10}{'Grade':<6}")

    for i in range(len(names)):
        print(f"{ids[i]:<5}{names[i]:<15}{ages[i]:<5}{courses[i]:<10}{grades[i]:<6.2f}")


def update_student(names, ages, courses, grades, ids):
    try:
        id_input = int(input("ID to update: "))

        if id_input in ids:
            i = ids.index(id_input)

            names[i] = prompt_non_empty("Name: ")
            ages[i] = prompt_age("Age: ")
            courses[i] = prompt_non_empty("Course: ")
            grades[i] = prompt_grade("Grade: ")

            save_data(names, ages, courses, grades, ids)
            print("Updated!")

        else:
            print("Not found.")

    except:
        print("Invalid input.")


def delete_student(names, ages, courses, grades, ids):
    try:
        id_input = int(input("ID to delete: "))

        if id_input in ids:
            i = ids.index(id_input)

            confirm = input("Delete? (yes/no): ")

            if confirm.lower() == "yes":
                for arr in (names, ages, courses, grades, ids):
                    arr.pop(i)

                save_data(names, ages, courses, grades, ids)
                print("Deleted!")

    except:
        print("Invalid input.")


def search_student(names, ages, courses, grades):

    key = input("Search name: ").lower()

    found = False

    for i in range(len(names)):
        if key in names[i].lower():
            print(names[i], courses[i], grades[i])
            found = True

    if not found:
        print("No match.")


def sort_students(names, ages, courses, grades, ids):

    combined = list(zip(ids, names, ages, courses, grades))
    combined.sort(key=lambda x: x[1])

    ids[:], names[:], ages[:], courses[:], grades[:] = zip(*combined)

    save_data(names, ages, courses, grades, ids)
    print("Sorted!")


def statistics(names, courses, grades):

    print_header("STUDENT STATISTICS")

    if len(names) == 0:
        print("No records.")
        return

    total = len(names)

    passed = len([g for g in grades if g >= 75])
    failed = total - passed

    avg = sum(grades) / total

    highest = max(grades)
    lowest = min(grades)

    print("Total:", total)
    print("Passed:", passed)
    print("Failed:", failed)
    print("Average:", avg)

    print("\nTop Students")

    students = list(zip(names, courses, grades))
    students.sort(key=lambda x: x[2], reverse=True)

    for i in range(min(3, len(students))):
        print(i+1, students[i])


def register():

    print_header("REGISTER")

    username = input("Username: ")
    password = input("Password: ")

    role = input("Role (admin/user): ").strip().lower()

    if role not in ["admin", "user"]:
        role = "user"

    with open(ACCOUNT_FILE, "a") as f:
        f.write(f"{username},{password},{role}\n")

    print("Account created!")


def login():

    print_header("LOGIN")

    while True:

        username = input("Username: ")
        password = input("Password: ")

        try:
            with open(ACCOUNT_FILE, "r") as f:
                for line in f:
                    data = line.strip().split(",")

                    if len(data) == 3:
                        user, pwd, role = data

                        if username.lower() == user.lower() and password == pwd:
                            print("\nLogin successful!")
                            print("Role:", role.lower())
                            return user, role.lower()

            print("\nInvalid login. Try again.\n")

        except FileNotFoundError:
            print("\nNo accounts found. Creating new account...\n")
            register()


def change_password(current_user):

    users = []

    try:
        with open(ACCOUNT_FILE, "r") as f:
            for line in f:
                users.append(line.strip().split(","))

        old = input("Old password: ")
        new = input("New password: ")

        for u in users:
            if u[0] == current_user:
                if u[1] != old:
                    print("Wrong password")
                    return
                u[1] = new

        with open(ACCOUNT_FILE, "w") as f:
            for u in users:
                f.write(",".join(u) + "\n")

        print("Password updated!")

    except:
        print("Error")