# subject_manager.py
from src.core_types.subject import Subject
import openpyxl

class SubjectManager:
    def __init__(self, subjects_data=None, subjects_file="subjects.xlsx"):
        self.subjects = subjects_data if subjects_data is not None else []
        self.subjects_file = subjects_file

    def validate_subject_code(self, subject_code):
        if not subject_code.strip():
            return False, "Mã môn học không được để trống."
        if self.find_subject_by_code(subject_code):
            return False, "Mã môn học đã tồn tại."
        return True, ""

    def find_subject_by_code(self, subject_code):
        for subject in self.subjects:
            if subject.subject_code == subject_code:
                return subject
        return None

    def add_subject(self, subject):
        self.subjects.append(subject)
        print("✓ Thêm môn học thành công!")

    def edit_subject(self, subject_code, new_info):
        subject = self.find_subject_by_code(subject_code)
        if subject:
            if 'subject_name' in new_info:
                subject.subject_name = new_info['subject_name']
            if 'credits' in new_info:
                try:
                    subject.credits = int(new_info['credits'])
                except ValueError:
                    print("Số tín chỉ phải là một số nguyên.")
            print("✓ Cập nhật thông tin môn học thành công!")
        else:
            print("Không tìm thấy môn học!")

    def delete_subject(self, subject_code):
        initial_len = len(self.subjects)
        self.subjects = [s for s in self.subjects if s.subject_code != subject_code]
        if len(self.subjects) < initial_len:
            print("✓ Xóa môn học thành công!")
            return True
        else:
            print("Không tìm thấy môn học!")
            return False

    def display_all_subjects(self):
        if not self.subjects:
            print("Không có môn học nào trong hệ thống.")
            return
        print("\n" + "="*50)
        print("{:<15} {:<30} {:<10}".format("Mã môn học", "Tên môn học", "Tín chỉ"))
        print("="*50)
        for subject in self.subjects:
            print("{:<15} {:<30} {:<10}".format(subject.subject_code, subject.subject_name, subject.credits))
        print("="*50)

    def load_subjects_from_excel(self):
        subjects = []
        try:
            workbook = openpyxl.load_workbook(self.subjects_file)
            sheet = workbook.active
            header = [cell.value for cell in sheet[1]]
            for row in sheet.iter_rows(min_row=2, values_only=True):
                if all(row):
                    subject_data = dict(zip(header, row))
                    subjects.append(Subject.from_dict(subject_data))
            print("✓ Tải dữ liệu môn học thành công!")
        except FileNotFoundError:
            print(f"Không tìm thấy file môn học: {self.subjects_file}")
        except Exception as e:
            print(f"Lỗi khi đọc file môn học: {e}")
        self.subjects = subjects

    def save_subjects_to_excel(self):
        try:
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            header = ['subject_code', 'subject_name', 'credits']
            sheet.append(header)
            for subject in self.subjects:
                sheet.append([subject.subject_code, subject.subject_name, subject.credits])
            workbook.save(self.subjects_file)
            print("✓ Lưu dữ liệu môn học thành công!")
            return True
        except Exception as e:
            print(f"Lỗi khi lưu file môn học: {e}")
            return False