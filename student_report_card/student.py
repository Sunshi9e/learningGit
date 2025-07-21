class Student:
    def __init__(self, name, subjects_scores):
        self.name = name
        self.subjects = subjects_scores  # a dictionary of subject: score
        self.average = self.calculate_average()
        self.grade = self.calculate_grade()

    def calculate_average(self):
        total = sum(self.subjects.values())
        count = len(self.subjects)
        return total / count if count > 0 else 0

    def calculate_grade(self):
        avg = self.average
        if avg >= 70:
            return 'A'
        elif avg >= 60:
            return 'B'
        elif avg >= 50:
            return 'C'
        elif avg >= 40:
            return 'D'
        else:
            return 'F'

    def to_dict(self):
        return {
            "name": self.name,
            "subjects": self.subjects,
            "average": self.average,
            "grade": self.grade
        }
