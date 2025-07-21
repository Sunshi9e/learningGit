import json
import os
from student import Student

DATABASE = "students.json"

def load_students():
    if not os.path.exists(DATABASE):
        return []
    try:
        with open(DATABASE, "r") as f:
            data = json.load(f)
            return [Student(d["name"], d["subjects"]) for d in data]
        
            # Equivalent to:
            # students = []
            # for d in data:
            #     name = d["name"]
            #     subjects = d["subjects"]
            #     student = Student(name, subjects)
            #     students.append(student)
            # return students
            # where data looks like this 👇
            # [ 
            # {"name": "Alice", "subjects": {"Math": 80, "English": 90}},
            #  {"name": "Bob", "subjects": {"Math": 60, "English": 70}} 
            # ]

    except (json.JSONDecodeError, FileNotFoundError):
        print("Error loading student records. Starting with an empty database.")
        return []


def save_students(students):
    try:
        with open(DATABASE, "w") as f:
            json.dump([s.to_dict() for s in students], f, indent=2)
            #same thing I did for load_student() but in reverse
    except IOError:
        print("Error saving student records.")

def find_student(name, students):
    for s in students:
        if s.name.lower() == name.lower():
            return s
    return None
