class Student:
    def __init__(self, student_id, name, birth_date, major, gender, course, faculty, class_name):
        self.student_id = student_id
        self.name = name
        self.birth_date = birth_date
        self.major = major
        self.gender = gender
        self.course = course
        self.faculty = faculty
        self.class_name = class_name
        self.scores = {}
        self.gpa = 0
        self.grade = "N/A"

    def add_score(self, subject, score):
        self.scores[subject] = [score]

    def calculate_gpa(self, system):
        total_points = 0
        total_credits = 0
        for subject_code, scores in self.scores.items():
            subject = system.subject_manager.find_subject_by_code(subject_code)
            if subject and scores:
                credits = subject.credits
                average_score = sum(scores) / len(scores)
                total_points += average_score * credits
                total_credits += credits
        self.gpa = total_points / total_credits if total_credits > 0 else 0
        return self.gpa

    def assign_grade(self):
        if self.gpa >= 9.5:
            self.grade = "A+"
        elif self.gpa >= 8.5:
            self.grade = "A"
        elif self.gpa >= 8.0:
            self.grade = "B+"
        elif self.gpa >= 7.0:
            self.grade = "B"
        elif self.gpa >= 6.5:
            self.grade = "C+"
        elif self.gpa >= 5.5:
            self.grade = "C"
        elif self.gpa >= 5.0:
            self.grade = "D+"
        elif self.gpa >= 4.0:
            self.grade = "D"
        else:
            self.grade = "F"
        return self.grade

    def to_dict(self):
        return {
            'student_id': self.student_id,
            'name': self.name,
            'birth_date': self.birth_date,
            'major': self.major,
            'gender': self.gender,
            'course': self.course,
            'faculty': self.faculty,
            'class_name': self.class_name,
            'scores': self.scores
        }

    @classmethod
    def from_dict(cls, data):
        student = cls(data['student_id'], data['name'], data['birth_date'], data['major'],
                    data['gender'], data['course'], data['faculty'], data['class_name'])
        student.scores = data.get('scores', {})
        return student