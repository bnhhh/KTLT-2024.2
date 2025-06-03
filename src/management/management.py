# student_management.py
from src.managers.student_manager import StudentManager
from src.managers.score_manager import ScoreManager
from src.managers.subject_manager import SubjectManager
from src.management.menu_handler import run_student_management, run_score_management, run_subject_management

class StudentManagementSystem:
    def __init__(self):
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
            score = score_data['total_score'] # Lấy điểm tổng kết
            student = self.student_manager.find_student_by_id(student_id)
            if student:
                student.add_score(subject_code, score)

        self.subject_credits = self.get_subject_credits_from_manager()

    def get_subject_credits_from_manager(self):
        credits = {}
        for subject in self.subject_manager.subjects:
            credits[subject.subject_code] = subject.credits
        return credits

    def save_data(self):
        """Lưu dữ liệu (ghi vào file Excel)"""
        self.student_manager.save_students_to_excel()
        self.score_manager.save_scores_to_excel()
        self.subject_manager.save_subjects_to_excel()
        print("Dữ liệu đã được lưu vào file Excel.")

    def add_student(self, student):
        """Thêm sinh viên mới"""
        is_valid_id, message = self.student_manager.validate_student_id(student.student_id)
        if not is_valid_id:
            print(message)
            return False
        self.student_manager.add_student(student)
        print("✓ Thêm sinh viên thành công!")
        return True

    def edit_student(self, student_id, new_info):
        """Sửa thông tin sinh viên"""
        is_valid_id, message = self.student_manager.validate_student_id(new_info.get('student_id'), exclude_id=student_id)
        if new_info.get('student_id') and not is_valid_id:
            print(message)
            return False
        student = self.student_manager.find_student_by_id(student_id)
        if student:
            for key, value in new_info.items():
                setattr(student, key, value)
            print("✓ Cập nhật thông tin thành công!")
        else:
            print("Không tìm thấy sinh viên!")

    def run(self):
        """Hàm chạy chính của chương trình"""
        while True:
            print("\n" + "="*60)
            print("                  HỆ THỐNG QUẢN LÝ SINH VIÊN VÀ ĐIỂM SỐ")
            print("="*60)
            print("1. Quản lý sinh viên")
            print("2. Quản lý điểm số")
            print("3. Quản lý môn học")
            print("10. Lưu dữ liệu")
            print("0. Thoát chương trình")
            print("="*60)
            main_choice = input("Chọn menu: ").strip()

            if main_choice == '1':
                run_student_management(self)
            elif main_choice == '2':
                run_score_management(self)
            elif main_choice == '3':
                run_subject_management(self)
            elif main_choice == '10':
                self.save_data()
            elif main_choice == '0':
                print("Cảm ơn đã sử dụng chương trình!")
                break
            else:
                print("Lựa chọn không hợp lệ!")