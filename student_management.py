# Simple Student Management System (CLI)
# Suitable for an internship beginner project

students = {}


def add_student():
    student_id = input("Enter student ID: ")
    if student_id in students:
        print("Student already exists!\n")
        return
    name = input("Enter student name: ")
    course = input("Enter course: ")
    students[student_id] = {
        "name": name,
        "course": course
    }
    print("Student added successfully!\n")


def view_students():
    if not students:
        print("No students found.\n")
        return
    print("--- Student List ---")
    for sid, info in students.items():
        print(f"ID: {sid} | Name: {info['name']} | Course: {info['course']}")
    print()


def search_student():
    student_id = input("Enter student ID to search: ")
    student = students.get(student_id)
    if student:
        print(f"Found: {student['name']} - {student['course']}\n")
    else:
        print("Student not found.\n")


def delete_student():
    student_id = input("Enter student ID to delete: ")
    if student_id in students:
        del students[student_id]
        print("Student deleted successfully!\n")
    else:
        print("Student not found.\n")


def menu():
    while True:
        print("Student Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


menu()
