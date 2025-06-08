"""
Module Quản lý Hệ thống Sinh viên

Module này chứa lớp StudentManagementSystem, là lớp trung tâm điều phối toàn bộ hệ thống.
Lớp này kết nối và điều phối các thành phần quản lý sinh viên, môn học và điểm số.

Các thành phần chính:
- StudentManager: Quản lý thông tin sinh viên
- ScoreManager: Quản lý điểm số
- SubjectManager: Quản lý môn học
"""

from managers.student_manager import StudentManager
from managers.score_manager import ScoreManager
from managers.subject_manager import SubjectManager
from utils.validation_utils import validate_student_id, validate_subject_code, validate_subject_name, validate_credits

class StudentManagementSystem:
    """
    Lớp trung tâm quản lý hệ thống sinh viên.
    
    Lớp này đóng vai trò điều phối giữa các thành phần quản lý:
    - Quản lý sinh viên (StudentManager)
    - Quản lý điểm số (ScoreManager)
    - Quản lý môn học (SubjectManager)
    
    Attributes:
        students_file (str): Đường dẫn file Excel lưu thông tin sinh viên
        scores_file (str): Đường dẫn file Excel lưu điểm số
        subjects_file (str): Đường dẫn file Excel lưu thông tin môn học
        student_manager (StudentManager): Quản lý sinh viên
        score_manager (ScoreManager): Quản lý điểm số
        subject_manager (SubjectManager): Quản lý môn học
        subject_credits (dict): Dictionary lưu số tín chỉ của từng môn học
    """

    def __init__(self):
        """
        Khởi tạo hệ thống quản lý sinh viên.
        
        Quy trình khởi tạo:
        1. Thiết lập đường dẫn các file Excel
        2. Khởi tạo các manager
        3. Load dữ liệu từ file Excel
        4. Liên kết điểm số với sinh viên
        5. Tạo dictionary số tín chỉ môn học
        """
        self.students_file = "students.xlsx"
        self.scores_file = "scores.xlsx"
        self.subjects_file = "subjects.xlsx"
        self.student_manager = StudentManager(students_file=self.students_file)
        self.score_manager = ScoreManager(scores_file=self.scores_file)
        self.subject_manager = SubjectManager(subjects_file=self.subjects_file)

        self.student_manager.load_students_from_excel()
        self.score_manager.load_scores_from_excel()
        self.subject_manager.load_subjects_from_excel()

        # Liên kết điểm số với sinh viên
        for score_data in self.score_manager.scores:
            student_id = score_data['student_id']
            subject_code = score_data['subject_code']
            score = score_data['total_score']
            student = self.student_manager.find_student_by_id(student_id)
            if student:
                student.add_score(subject_code, score)

        self.subject_credits = self.get_subject_credits_from_manager()

    def get_subject_credits_from_manager(self):
        """
        Tạo dictionary lưu số tín chỉ của từng môn học.
        
        Returns:
            dict: Dictionary với key là mã môn học, value là số tín chỉ
        """
        credits = {}
        for subject in self.subject_manager.subjects:
            credits[subject.subject_code] = subject.credits
        return credits

    def save_data(self):
        """
        Lưu toàn bộ dữ liệu vào các file Excel.
        
        Lưu lần lượt:
        1. Thông tin sinh viên
        2. Điểm số
        3. Thông tin môn học
        """
        self.student_manager.save_students_to_excel()
        self.score_manager.save_scores_to_excel()
        self.subject_manager.save_subjects_to_excel()
        print("Dữ liệu đã được lưu vào file Excel.")

    def add_student(self, student):
        """
        Thêm sinh viên mới vào hệ thống.
        
        Args:
            student: Đối tượng Student cần thêm
            
        Returns:
            bool: True nếu thêm thành công, False nếu thất bại
        """
        is_valid_id, message = validate_student_id(student.student_id, existing_students=self.student_manager.students)
        if not is_valid_id:
            print(message)
            return False
        if self.student_manager.add_student(student):
            print("✓ Thêm sinh viên thành công!")
            return True
        return False

    def edit_student(self, student_id, new_info):
        """
        Sửa thông tin sinh viên.
        
        Args:
            student_id (str): MSSV của sinh viên cần sửa
            new_info (dict): Dictionary chứa thông tin mới
            
        Returns:
            bool: True nếu sửa thành công, False nếu thất bại
        """
        return self.student_manager.edit_student(student_id, new_info)

    def add_subject(self, subject):
        """
        Thêm môn học mới vào hệ thống.
        
        Args:
            subject: Đối tượng Subject cần thêm
            
        Returns:
            bool: True nếu thêm thành công, False nếu thất bại
        """
        is_valid_code, code_message = validate_subject_code(subject.subject_code, existing_subjects=self.subject_manager.subjects)
        if not is_valid_code:
            print(code_message)
            return False
        if self.subject_manager.add_subject(subject):
            print("✓ Thêm môn học thành công!")
            return True
        return False