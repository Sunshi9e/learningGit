from utils import load_students, save_students, find_student
from student import Student

def add_student():
    name = input("Enter student name: ")
    students = load_students()

    if find_student(name, students):
        print("Student already exists. Use update option instead.")
        return

    subjects_scores = {}
    while True:
        subject = input("Enter subject (or 'done' to finish): ")
        if subject.lower() == "done":
            break
        try:
            score = float(input(f"Enter score for {subject}: "))
            if score < 0 or score > 100:
                print("Score must be between 0 and 100.")
                continue
            subjects_scores[subject] = score
        except ValueError:
            print("Invalid input. Please enter a number.")

    if subjects_scores:
        new_student = Student(name, subjects_scores)
        students.append(new_student)
        save_students(students)
        print(f"{name} added successfully.")

def view_students():
    students = load_students()
    if not students:
        print("No students found.")
        return

    for student in students:
        print("-" * 30)
        print(f"Name    : {student.name}")
        print(f"Average : {student.average:.2f}")
        print(f"Grade   : {student.grade}")
        print("Subjects and Scores:")
        for subject, score in student.subjects.items():
            print(f"  {subject}: {score}")
    print("-" * 30)

def update_student():
    name = input("Enter student name to update: ")
    students = load_students()
    student = find_student(name, students)

    if not student:
        print("Student not found.")
        return

    print("Leave score empty if no change.")
    for subject in student.subjects:
        try:
            new_score = input(f"New score for {subject} (current: {student.subjects[subject]}): ")
            if new_score:
                student.subjects[subject] = float(new_score)
        except ValueError:
            print("Invalid input. Skipping this subject.")

    student.average = student.calculate_average()
    student.grade = student.calculate_grade()
    save_students(students)
    print(f"{student.name}'s record updated.")

def delete_student():
    name = input("Enter student name to delete: ")
    students = load_students()
    student = find_student(name, students)

    if not student:
        print("Student not found.")
        return

    students.remove(student)
    save_students(students)
    print(f"{name} has been deleted.")

def main():
    while True:
        print("\n--- Student Record Manager ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
