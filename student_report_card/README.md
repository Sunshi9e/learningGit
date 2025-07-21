#  Student Record Manager

A simple and interactive command-line application in Python to manage student academic records. It supports adding, viewing, updating, and deleting students, while automatically calculating averages and assigning grades.

---

##  Features

- ✅ Add, view, update, and delete student records
- ✅ Track scores across multiple subjects
- ✅ Automatically calculates average scores
- ✅ Grade assignment based on average
- ✅ Persistent storage using a `students.json` file
- ✅ Command-line interface with menu options

---

##  Grade Scale

| Average Score | Letter Grade |
|---------------|--------------|
| 70+           | A            |
| 60 - 69       | B            |
| 50 - 59       | C            |
| 40 - 49       | D            |
| Below 40      | F            |

---

## 🧩 File Structure

student-record-manager/

├── main.py 

├── student.py 

├── utils.py

├── students.json

└── README.md


---

## 🛠 Requirements

- Python 3.6 or higher
- No external libraries required

---

## ▶️ Running the App

```bash
python main.py
```

--- Student Record Manager ---
1. Add Student
2. View All Students
3. Update Student
4. Delete Student
5. Exit

###  Add a Student

* Select option 1 from the menu

* Enter the student's name

* Enter subjects and scores

* Type done to finish

```
Enter student name: Alice
Enter subject (or 'done' to finish): Math
Enter score for Math: 80
Enter subject (or 'done' to finish): English
Enter score for English: 75
Enter subject (or 'done' to finish): done
Alice added successfully.
```

###  View All Students

* Choose option 2 to view all stored students. Output includes:

* Student name

* Subjects and scores

* Average score

* Letter grade

Example Output:
```
------------------------------
Name    : Alice
Average : 77.50
Grade   : A
Subjects and Scores:
  Math: 80.0
  English: 75.0
------------------------------
```

###  Update a Student

* Choose option 3

* Enter the student's name

* Enter new scores or leave blank to skip

* Example:

```
Enter student name to update: Alice
New score for Math (current: 80.0):
New score for English (current: 75.0): 85
Alice's record updated.
```
### Delete a Student

* Choose option 4

* Enter the student’s name

* Confirm deletion

Example:

```
Enter student name to delete: Alice
Alice has been deleted.
```

### Error Handling

* Prevents duplicate student names

* Handles invalid input (e.g., non-numeric scores)

* Validates score ranges (0–100)

* Handles missing or corrupted data files gracefully

## Student Class Overview

* Location: student.py

### Attributes:

* name – Student's name

* subjects – Dictionary of subjects and scores

* average – Automatically calculated

* grade – Based on average

### Key Methods:

* calculate_average() – Computes average from subject scores

* calculate_grade() – Assigns grade based on average

* to_dict() – Converts object to savable JSON format

## Final Notes

This project is ideal for practicing:

* File handling in Python

* Object-oriented programming

* CLI interaction

* JSON data persistence

* Enjoy managing your student records!