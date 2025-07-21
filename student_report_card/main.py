import json
import os
from student import Student

DataBase = "students.json"

def add_student():
    name = input("Enter student name: ").strip()
    subjects = {}

    while True:
        subject = input("Enter subject (or 'done' to finish): ").strip()
        if subject.lower() == 'done':
            break
        try:
            score = float(input(f"Enter score for {subject}: "))
            subjects[subject] = score
        except ValueError:
            print("Invalid score. Please enter a number.")

    student = Student(name, subjects)
    student_data = student.to_dict()

    students = []
    if os.path.exists(DataBase):
        with open(DataBase, 'r') as f:
            students = json.load(f)

    students.append(student_data)

    with open(DataBase, 'w') as f:
        json.dump(students, f, indent=2)

    print(f"\n{name}'s record saved successfully.\n")

def main():
    while True:
        print("\n1. Add Student\n2. View All Students\n3. Update Student\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("That option isn't ready yet.\n")

if __name__ == "__main__":
    main()
