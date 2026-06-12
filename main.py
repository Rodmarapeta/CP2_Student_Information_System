from file_handler import load_data
from student_functions import *

names, ages, courses, grades, ids = load_data()


def start_menu():
    print("\n==============================")
    print("  WELCOME TO SYSTEM")
    print("==============================")
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    print("==============================")

while True:

    start_menu()
    choice = input("Choose option: ")

    if choice == "1":
        current_user, role = login()
        break

    elif choice == "2":
        register()
        print("\nYou can now login.\n")

    elif choice == "3":
        print("Goodbye!")
        exit()

    else:
        print("Invalid choice.")

while True:

    show_menu(role)
    choice = input("Choice: ")

    if role == "admin":

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
            change_password(current_user)

        elif choice == "9":
            print("\nLogging out...")
            current_user, role = login()

        elif choice == "10":
            confirm = input("Exit? (yes/no): ").strip().lower()

            if confirm in ["yes", "y"]:
                print("\nGoodbye!")
                break
            else:
                print("\nExit cancelled.")

        else:
            print("\nInvalid choice.")

    else:

        if choice == "1":
            view_students(names, ages, courses, grades, ids)

        elif choice == "2":
            search_student(names, ages, courses, grades)

        elif choice == "3":
            statistics(names, courses, grades)

        elif choice == "4":
            change_password(current_user)

        elif choice == "5":
            print("\nLogging out...")
            current_user, role = login()

        elif choice == "6":
            confirm = input("Exit? (yes/no): ").strip().lower()

            if confirm in ["yes", "y"]:
                print("\nGoodbye!")
                break
            else:
                print("\nExit cancelled.")

        else:
            print("\nInvalid choice.")