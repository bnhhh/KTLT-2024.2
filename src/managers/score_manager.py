from utils.file_utils import ExcelFileHandler
from utils.score_utils import validate_score, calculate_final_score, get_grade

class ScoreManager:
    def __init__(self, scores_data=None, scores_file="scores.xlsx"):
        self.scores = scores_data if scores_data is not None else []
        self.scores_file = scores_file

    def find_score_record(self, student_id, subject_code):
        """Tìm kiếm bản ghi điểm"""
        for score in self.scores:
            if score['student_id'] == student_id and score['subject_code'] == subject_code:
                return score
        return None

    def add_score(self, score_record):
        """Nhập điểm cho sinh viên"""
        total_score = calculate_final_score(
            score_record['attendance_score'],
            score_record['midterm_score'],
            score_record['final_score']
        )
        score_record['total_score'] = round(total_score, 2)
        score_record['grade'] = get_grade(total_score)
        
        self.scores.append(score_record)
        print(f"✓ Nhập điểm thành công!")
        print(f"Điểm tổng kết: {score_record['total_score']}")
        print(f"Xếp loại: {score_record['grade']}")

    def edit_score(self, student_id, subject_code, new_scores):
        """Cập nhật điểm sinh viên"""
        score_record = self.find_score_record(student_id, subject_code)
        if score_record:
            score_record.update(new_scores)
            total_score = calculate_final_score(
                score_record['attendance_score'],
                score_record['midterm_score'],
                score_record['final_score']
            )
            score_record['total_score'] = round(total_score, 2)
            score_record['grade'] = get_grade(total_score)
            
            print("✓ Cập nhật điểm thành công!")
            print(f"Điểm tổng kết mới: {score_record['total_score']}")
            print(f"Xếp loại mới: {score_record['grade']}")
        else:
            print("Không tìm thấy bản ghi điểm!")

    def delete_score(self, student_id, subject_code):
        """Xóa điểm"""
        initial_len = len(self.scores)
        self.scores = [s for s in self.scores if not (s['student_id'] == student_id and s['subject_code'] == subject_code)]
        if len(self.scores) < initial_len:
            print("✓ Xóa điểm thành công!")
            return True
        else:
            print("Không tìm thấy bản ghi điểm!")
            return False

    def view_student_scores(self, student_id, students):
        """Xem điểm của một sinh viên"""
        student = next((s for s in students if s.student_id == student_id), None)
        if not student:
            print("Không tìm thấy sinh viên!")
            return
        student_scores = [s for s in self.scores if s['student_id'] == student_id]
        if not student_scores:
            print("Sinh viên này chưa có điểm nào!")
            return
        print(f"\nBảng điểm sinh viên: {student.name} - {student_id}")
        print("-" * 100)
        print(f"{'Mã HP':<10} {'Tên Môn Học':<25} {'CC':<5} {'GK':<5} {'CK':<5} {'TK':<5} {'Loại':<5}")
        print("-" * 100)
        for score in student_scores:
            subject_code = score['subject_code']
            print(f"{subject_code:<10} {subject_code:<25} {score['attendance_score']:<5} "
                  f"{score['midterm_score']:<5} {score['final_score']:<5} {score['total_score']:<5} {score['grade']:<5}")
        print("-" * 100)

    def view_subject_scores(self, subject_code, students):
        """Xem điểm một môn của tất cả sinh viên"""
        subject_scores = [s for s in self.scores if s['subject_code'] == subject_code]
        if not subject_scores:
            print("Môn học này chưa có điểm nào!")
            return
        print(f"\nBảng điểm môn học: {subject_code}")
        print("-" * 90)
        print(f"{'MSSV':<10} {'Họ tên':<25} {'CC':<5} {'GK':<5} {'CK':<5} {'TK':<5} {'Loại':<5}")
        print("-" * 90)
        for score in subject_scores:
            student = next((s for s in students if s.student_id == score['student_id']), None)
            student_name = student.name if student else "N/A"
            print(f"{score['student_id']:<10} {student_name:<25} {score['attendance_score']:<5} "
                  f"{score['midterm_score']:<5} {score['final_score']:<5} {score['total_score']:<5} {score['grade']:<5}")
        print("-" * 90)
        total_scores = [s['total_score'] for s in subject_scores]
        avg_score = sum(total_scores) / len(total_scores) if total_scores else 0
        max_score = max(total_scores) if total_scores else "N/A"
        min_score = min(total_scores) if total_scores else "N/A"
        print(f"Số sinh viên: {len(subject_scores)}")
        print(f"Điểm trung bình: {round(avg_score, 2)}")
        print(f"Điểm cao nhất: {max_score}")
        print(f"Điểm thấp nhất: {min_score}")

    def display_score_info(self, score_record, students):
        """Hiển thị thông tin điểm"""
        student = next((s for s in students if s.student_id == score_record['student_id']), None)
        student_name = student.name if student else "N/A"
        print(f"Sinh viên: {student_name} ({score_record['student_id']})")
        print(f"Mã học phần: {score_record['subject_code']}")
        print(f"Điểm chuyên cần: {score_record['attendance_score']}")
        print(f"Điểm giữa kỳ: {score_record['midterm_score']}")
        print(f"Điểm cuối kỳ: {score_record['final_score']}")
        print(f"Điểm tổng kết: {score_record['total_score']}")
        print(f"Xếp loại: {score_record['grade']}")

    def load_scores_from_excel(self):
        """Đọc dữ liệu điểm số từ file Excel"""
        self.scores = ExcelFileHandler.load_from_excel(self.scores_file)

    def save_scores_to_excel(self):
        """Lưu dữ liệu điểm số vào file Excel"""
        headers = ['student_id', 'subject_code', 'attendance_score', 'midterm_score', 'final_score', 'total_score', 'grade']
        return ExcelFileHandler.save_to_excel(self.scores_file, self.scores, headers)

    def delete_scores_by_subject(self, subject_code):
        """Xóa tất cả điểm của một môn học"""
        initial_len = len(self.scores)
        self.scores = [s for s in self.scores if s['subject_code'] != subject_code]
        if len(self.scores) < initial_len:
            print(f"Đã xóa tất cả điểm của môn học {subject_code}.")