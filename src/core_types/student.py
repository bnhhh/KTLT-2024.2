from utils.score_utils import calculate_gpa, get_grade

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

    def add_score(self, subject_code, score):
        """Thêm điểm cho môn học"""
        self.scores[subject_code] = score

    def calculate_gpa(self, system):
        """Tính điểm trung bình tích lũy (GPA)"""
        if not self.scores:
            return 0.0
        self.gpa = calculate_gpa(self.scores, system.subject_credits)
        self.grade = get_grade(self.gpa)
        return self.gpa

    def to_dict(self):
        """
        Chuyển đổi đối tượng sinh viên sang định dạng từ điển
        Returns:
            dict: từ điển chứa thông tin sinh viên
        """
        return {
            'student_id': self.student_id,
            'name': self.name,
            'birth_date': self.birth_date,
            'gender': self.gender,
            'course': self.course,
            'faculty': self.faculty,
            'class_name': self.class_name,
            'major': self.major
        }

    @classmethod
    def from_dict(cls, data):
        """
        Tạo đối tượng Student từ dữ liệu từ điển
        Tham số:
            data (dict): Từ điển chứa thông tin sinh viên
        Trả về:
            Student: Một đối tượng Student mới được khởi tạo
        """
        return cls(
            data['student_id'],
            data['name'],
            data['birth_date'],
            data['major'],
            data['gender'],
            data['course'],
            data['faculty'],
            data['class_name']
        )