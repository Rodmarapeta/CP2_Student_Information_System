from file_handler import load_data
from student_functions import *

names, ages, courses, grades, ids = load_data()

login()

print_header("STUDENT INFORMATION SYSTEM")

while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        add_student(names, ages, courses, grades, ids)

    elif choice == "2":
        view_students(names, ages, courses, grades, ids)

    elif choice == "3":
        update_student(names, ages, courses, grades, ids)

    elif choice == "4":
        delete_student(names, ages, courses, grades, ids)

    elif choice == "5":
        search_student(names, ages, courses, grades)

    elif choice == "6":
        sort_students(names, ages, courses, grades, ids)

    elif choice == "7":
        statistics(names, courses, grades)

    elif choice == "8":
        print("\n  Thank you for using the system!\n")
        break

    else:
        print("\n  [!] Invalid choice. Enter 1-8.")