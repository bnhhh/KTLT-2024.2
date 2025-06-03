# student_manager.py
from src.core_types.student import Student
from datetime import datetime
import openpyxl

def validate_date(date_str):
    """Validate ngày sinh"""
    try:
        datetime.strptime(date_str, "%d/%m/%Y")
        return True, ""
    except ValueError:
        return False, "Ngày sinh phải có định dạng dd/mm/yyyy"

def is_valid_student_id(student_id):
    return student_id.isdigit() and len(student_id) == 8

def is_valid_name(name):
    for char in name:
        if not ('a' <= char <= 'z' or 'A' <= char <= 'Z' or ' ' == char or 'À' <= char <= 'ỹ' or 'á' <= char <= 'ý' or 'Á' <= char <= 'Ý' or char in "ăâđêôơưĂÂĐÊÔƠƯ"):
            return False
    return True

class StudentManager:
    def __init__(self, students_data=None, students_file="students.xlsx"):
        self.students = students_data if students_data is not None else []
        self.students_file = students_file

    def validate_student_id(self, student_id, exclude_id=None):
        """Validate mã số sinh viên"""
        if not is_valid_student_id(student_id):
            return False, "MSSV phải là 8 chữ số"
        for student in self.students:
            if str(student.student_id) == student_id and student_id != exclude_id:
                return False, "MSSV đã tồn tại"
        return True, ""

    def validate_name(self, name):
        """Validate họ tên"""
        if not is_valid_name(name):
            return False, "Họ tên không hợp lệ"
        return True, ""

    def validate_gender(self, gender):
        """Validate giới tính"""
        if gender.lower() not in ['nam', 'nữ']:
            return False, "Giới tính phải là 'Nam' hoặc 'Nữ'"
        return True, ""

    def find_student_by_id(self, student_id):
        """Tìm sinh viên theo MSSV"""
        for student in self.students:
            if str(student.student_id) == student_id:
                return student
        return None

    def add_student(self, student):
        """Thêm sinh viên mới"""
        self.students.append(student)
        print("✓ Thêm sinh viên thành công!")

    def edit_student(self, student_id, new_info):
        """Sửa thông tin sinh viên"""
        student = self.find_student_by_id(student_id)
        if student:
            for key, value in new_info.items():
                setattr(student, key, value)
            print("✓ Cập nhật thông tin thành công!")
        else:
            print("Không tìm thấy sinh viên!")

    def delete_student(self, student_id):
        """Xóa sinh viên"""
        initial_len = len(self.students)
        self.students = [s for s in self.students if s.student_id != student_id]
        if len(self.students) < initial_len:
            print("✓ Xóa sinh viên thành công!")
            return True
        else:
            print("Không tìm thấy sinh viên!")
            return False

    def search_students(self, search_type, keyword):
        """Tìm kiếm sinh viên"""
        results = []
        if search_type == '1':
            results = [s for s in self.students if keyword.lower() in str(s.student_id).lower()]
        elif search_type == '2':
            results = [s for s in self.students if keyword.lower() in s.name.lower()]
        elif search_type == '3':
            results = [s for s in self.students if keyword.lower() in s.class_name.lower()]
            results.sort(key=lambda x: x.name)
        elif search_type == '4':
            results = [s for s in self.students if keyword.lower() in s.faculty.lower()]
            results.sort(key=lambda x: x.name)
        return results

    def display_student_info(self, student):
        """Hiển thị thông tin sinh viên"""
        print(f"MSSV: {student.student_id}")
        print(f"Họ tên: {student.name}")
        print(f"Ngày sinh: {student.birth_date}")
        print(f"Giới tính: {student.gender}")
        print(f"Khóa học: {student.course}")
        print(f"Khoa viện: {student.faculty}")
        print(f"Lớp: {student.class_name}")
        print(f"Ngành học: {student.major}")

    def display_all_students(self, show_gpa=False):
        """Hiển thị danh sách tất cả sinh viên"""
        if not self.students:
            print("Không có sinh viên nào trong hệ thống")
            return
        print(f"\n{'='*140}")
        print(f"{'DANH SÁCH SINH VIÊN':^140}")
        print(f"{'='*140}")
        header = "{:<10} {:<25} {:<12} {:<20} {:<8} {:<15} {:<20} {:<10}".format('Mã SV', 'Họ tên', 'Ngày sinh', 'Ngành', 'Giới tính', 'Khóa học', 'Khoa viện', 'Lớp')
        if show_gpa:
            header += " {:<10} {:<5}".format('GPA', 'Loại')
        print(header)
        print(f"{'-'*140}")
        for student in self.students:
            row = "{:<10} {:<25} {:<12} {:<20} {:<8} {:<15} {:<20} {:<10}".format(student.student_id, student.name, student.birth_date, student.major, student.gender, student.course, student.faculty, student.class_name)
            if show_gpa:
                row += " {:<10.2f} {:<5}".format(student.gpa, student.grade)
            print(row)

    def load_students_from_excel(self):
        """Load dữ liệu sinh viên từ file XLSX"""
        students = []
        try:
            workbook = openpyxl.load_workbook(self.students_file)
            sheet = workbook.active
            header = [cell.value for cell in sheet[1]]
            for row in sheet.iter_rows(min_row=2, values_only=True):
                if all(row):  # Check if the entire row is not None
                    students.append(Student.from_dict(dict(zip(header, row))))
            print("✓ Tải dữ liệu sinh viên thành công!")
        except FileNotFoundError:
            print(f"Không tìm thấy file sinh viên XLSX: {self.students_file}")
        except Exception as e:
            print(f"Lỗi khi đọc file sinh viên XLSX: {e}")
        self.students = students

    def save_students_to_excel(self):
        """Lưu dữ liệu sinh viên vào file XLSX"""
        try:
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            header = ['student_id', 'name', 'birth_date', 'gender', 'course', 'faculty', 'class_name', 'major']
            sheet.append(header)
            for student in self.students:
                sheet.append([student.student_id, student.name, student.birth_date, student.gender, student.course, student.faculty, student.class_name, student.major])
            workbook.save(self.students_file)
            print("✓ Lưu dữ liệu sinh viên thành công!")
            return True
        except Exception as e:
            print(f"Lỗi khi lưu file sinh viên XLSX: {e}")
            return False

    def sort_by_name(self):
        self.students.sort(key=lambda student: student.name)

    def sort_by_gpa(self):
        self.students.sort(key=lambda student: student.gpa, reverse=True)

    def sort_by_id(self):
        self.students.sort(key=lambda student: student.student_id)