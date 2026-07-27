import json
import os

students = []


def load_students():
    global students

    if os.path.exists("students.json"):
        with open("students.json", "r") as file:
            students = json.load(file)


def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)


def show_menu():
    print("================================")
    print("    Student Grade Manager")
    print("================================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    print()


def add_student():
    name = input("Enter student name: ")
    grade = input("Enter student grade: ")

    students.append([name, grade])
    save_students()

    print("\nStudent added successfully!")


def search_student():
    name = input("Enter student name to search: ")
    found = False

    for student in students:
        if student[0].lower() == name.lower():
            print(f"Found - Name: {student[0]}, Grade: {student[1]}")
            found = True
            break

    if not found:
        print("Student not found.")


def delete_student():
    name = input("Enter student name to delete: ")
    found = False

    for student in students:
        if student[0].lower() == name.lower():
            students.remove(student)
            save_students()
            print("Student deleted successfully!")
            found = True
            break

    if not found:
        print("Student not found.")


# تحميل البيانات السابقة عند بدء التشغيل
load_students()

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        print("\n===== Students List =====")
        if not students:
            print("No students found.")
        else:
            for student in students:
                print(f"Name: {student[0]}, Grade: {student[1]}")

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option!")