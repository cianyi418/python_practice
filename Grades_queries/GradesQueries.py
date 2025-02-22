# 建立一個學生管理系統，讓使用者：1：新增學生（姓名 & 分數）2：查詢特定學生的分數 3：顯示所有學生 4：離開程式 學生資料應該存入 students.json，每次關閉程式時仍能保存！

import json
import os

# Path to the JSON file
json_file_path = "students.json"

# Load the students grades from a JSON file
if os.path.exists(json_file_path):
    try:
        with open(json_file_path, "r", encoding= 'utf-8') as file:
            students_grades = json.load(file)
            if not isinstance(students_grades, dict):
                students_grades = {}
    except json.JSONDecodeError:
        students_grades = {}
        print("Error decoding JSON file. Starting with an empty student list.")
else:
    students_grades = {}
    print("JSON file not found. Starting with an empty student list.")

# Save the students grades to a JSON file
def save_students_grades():
    with open(json_file_path, "w", encoding='utf-8') as file:
        json.dump(students_grades, file, indent=4, ensure_ascii=False)
    print("Students' grades saved to", json_file_path)

# The showing all students display frame
def show_students():
    if not students_grades:
        print("No students found")
        return
    
    name_width = max(len(name) for name in students_grades) + 2
    print("\n Students Grades:")
    print("Name".ljust(name_width), "| Grade")
    print("=" * 20)
    for name, grade in sorted(students_grades.items(), key=lambda item: item[1
    ]):
        print(f"{name.ljust(name_width)} | {grade}")
    print("=" * 20)
    total, average = calculate_grades()
    print(f"Total grades: {total}")
    print(f"Average grade: {average:.1f}")

# Calculate the total and average grades
def calculate_grades():
    total = sum(students_grades.values())
    average = total / len(students_grades)
    return total, average
        

while True:
    print("\nChoose an option:")
    print("1. Add a student")
    print("2. Search for a student's grade")
    print("3. Show all students")
    print("4. Delete a student")
    print("5. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == '1':
        name = input("Enter the name of the student: ").strip()
        if not name:
            print("Name cannot be empty, please try again")
            continue
        if name.lower() in (student_name.lower() for student_name in students_grades):
            for student_name, grade in students_grades.items():
                if student_name.lower() == name.lower():
                    print(f"{student_name} already exists, the grade is {grade}")
                    break
        else:
            grade = input("Enter the grade: ").strip()
            if not grade.isdigit():
                print("Grade must be a number, please try again")
                continue

            students_grades[name] = int(grade)
            print(f"{name} added with a grade of {grade}")
            save_students_grades()

    elif choice == '2':
        name = input("Enter the name of the student: ").strip().lower()
        found = False
        for student_name, grade in students_grades.items():
            if student_name.lower() == name:
                print(f"{student_name}'s grade is {grade}")
                found = True
                break
        else:
            print(f"{name} not found in students")

    elif choice == '3':
        show_students()

    elif choice == '4':
        name = input("Enter the name of the student you want to delete: ").strip()
        found = False
        for student_name in list(students_grades.keys()):
            if student_name.lower() == name.lower():
                del students_grades[student_name]
                print(f"{student_name} has been deleted from students")
                save_students_grades()
                break
        else:
            print(f"{name} not found in students")

    elif choice == '5':
        print("Exiting...")
        break

    else:
        print("Invalid choice, please try again")
        