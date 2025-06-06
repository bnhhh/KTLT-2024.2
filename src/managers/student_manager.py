from core_types.student import Student
from datetime import datetime
import openpyxl
from utils.file_utils import ExcelFileHandler
from utils.validation_utils import (
    validate_date, validate_student_id, validate_name, validate_gender,
    validate_course, validate_faculty, validate_class_name, validate_major
)

def validate_date(date_str):
    """Validate ngày sinh"""
    if not date_str or not date_str.strip():
        return False, "Ngày sinh không được để trống"
    try:
        datetime.strptime(date_str, "%d/%m/%Y")
        return True, ""
    except ValueError:
        return False, "Ngày sinh phải có định dạng dd/mm/yyyy"

def is_valid_student_id(student_id):
    if not student_id:  # Kiểm tra nếu student_id là None hoặc rỗng
        return False
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
        """Kiểm tra tính hợp lệ của mã số sinh viên"""
        if not student_id:
            return False, "MSSV không được để trống"
        if not is_valid_student_id(student_id):
            return False, "MSSV phải là 8 chữ số"
        for student in self.students:
            if str(student.student_id) == student_id and student_id != exclude_id:
                return False, "MSSV đã tồn tại"
        return True, ""

    def validate_name(self, name):
        """Kiểm tra tính hợp lệ của họ tên"""
        if not name or not name.strip():
            return False, "Họ tên không được để trống"
        if not is_valid_name(name):
            return False, "Họ tên không hợp lệ"
        return True, ""

    def validate_gender(self, gender):
        """Kiểm tra tính hợp lệ của giới tính"""
        if not gender or not gender.strip():
            return False, "Giới tính không được để trống"
        if gender.lower() not in ['nam', 'nữ']:
            return False, "Giới tính phải là 'Nam' hoặc 'Nữ'"
        return True, ""

    def validate_course(self, course):
        """Kiểm tra tính hợp lệ của khóa học"""
        if not course or not course.strip():
            return False, "Khóa học không được để trống"
        return True, ""

    def validate_faculty(self, faculty):
        """Kiểm tra tính hợp lệ của khoa viện"""
        if not faculty or not faculty.strip():
            return False, "Khoa viện không được để trống"
        return True, ""

    def validate_class_name(self, class_name):
        """Kiểm tra tính hợp lệ của lớp"""
        if not class_name or not class_name.strip():
            return False, "Lớp không được để trống"
        return True, ""

    def validate_major(self, major):
        """Kiểm tra tính hợp lệ của ngành học"""
        if not major or not major.strip():
            return False, "Ngành học không được để trống"
        return True, ""

    def find_student_by_id(self, student_id):
        """Tìm kiếm sinh viên theo mã số sinh viên"""
        for student in self.students:
            if str(student.student_id) == student_id:
                return student
        return None

    def add_student(self, student):
        """Thêm sinh viên mới vào hệ thống"""
        # Kiểm tra tính hợp lệ của tất cả các trường
        validations = [
            validate_student_id(student.student_id, self.students),
            validate_name(student.name),
            validate_gender(student.gender),
            validate_date(student.birth_date),
            validate_course(student.course),
            validate_faculty(student.faculty),
            validate_class_name(student.class_name),
            validate_major(student.major)
        ]
        
        # Kiểm tra nếu có bất kỳ trường nào không hợp lệ
        for is_valid, message in validations:
            if not is_valid:
                print(f"Lỗi: {message}")
                return False
            
        # Nếu tất cả validation đều thành công, thêm sinh viên
        self.students.append(student)
        print("✓ Thêm sinh viên thành công!")
        return True

    def edit_student(self, student_id, new_info):
        """Cập nhật thông tin sinh viên"""
        if not student_id:
            print("MSSV không được để trống!")
            return False

        student = self.find_student_by_id(student_id)
        if not student:
            print("Không tìm thấy sinh viên!")
            return False

        # Kiểm tra mã số sinh viên mới nếu được cung cấp
        new_student_id = new_info.get('student_id')
        if new_student_id:
            is_valid_id, message = validate_student_id(new_student_id, self.students, exclude_id=student_id)
            if not is_valid_id:
                print(message)
                return False

        # Kiểm tra tất cả các trường được cập nhật
        validations = []
        for field in ['name', 'gender', 'birth_date', 'course', 'faculty', 'class_name', 'major']:
            if field in new_info:  # Kiểm tra nếu trường có trong new_info
                value = new_info[field]
                if field == 'name':
                    validations.append(validate_name(value))
                elif field == 'gender':
                    validations.append(validate_gender(value))
                elif field == 'birth_date':
                    validations.append(validate_date(value))
                elif field == 'course':
                    validations.append(validate_course(value))
                elif field == 'faculty':
                    validations.append(validate_faculty(value))
                elif field == 'class_name':
                    validations.append(validate_class_name(value))
                elif field == 'major':
                    validations.append(validate_major(value))

        # Kiểm tra nếu có bất kỳ trường nào không hợp lệ
        for is_valid, message in validations:
            if not is_valid:
                print(f"Lỗi: {message}")
                return False

        # Cập nhật thông tin sinh viên
        for key, value in new_info.items():
            if value is not None:
                setattr(student, key, value)
        print("✓ Cập nhật thông tin thành công!")
        return True

    def delete_student(self, student_id):
        """Xóa sinh viên khỏi hệ thống"""
        initial_len = len(self.students)
        self.students = [s for s in self.students if s.student_id != student_id]
        if len(self.students) < initial_len:
            print("✓ Xóa sinh viên thành công!")
            return True
        else:
            print("Không tìm thấy sinh viên!")
            return False

    def search_students(self, search_type, keyword):
        """Tìm kiếm sinh viên theo các tiêu chí khác nhau"""
        if not keyword:
            return []
            
        keyword = keyword.strip().lower()
        results = []
        
        try:
            if search_type == '1':  # Tìm theo MSSV
                results = [s for s in self.students if keyword in str(s.student_id).lower()]
            elif search_type == '2':  # Tìm theo tên
                results = [s for s in self.students if keyword in s.name.lower()]
            elif search_type == '3':  # Tìm theo lớp
                results = [s for s in self.students if keyword in s.class_name.lower()]
                results.sort(key=lambda x: x.name.lower())
            elif search_type == '4':  # Tìm theo khoa
                results = [s for s in self.students if keyword in s.faculty.lower()]
                results.sort(key=lambda x: x.name.lower())
            else:
                print("Loại tìm kiếm không hợp lệ!")
                return []
                
            if not results:
                print("Không tìm thấy kết quả phù hợp!")
            return results
            
        except Exception as e:
            print(f"Lỗi khi tìm kiếm: {str(e)}")
            return []

    def display_student_info(self, student):
        """Hiển thị thông tin chi tiết của một sinh viên"""
        print("\n" + "="*50)
        print(f"MSSV: {student.student_id}")
        print(f"Họ tên: {student.name}")
        print(f"Giới tính: {student.gender}")
        print(f"Ngày sinh: {student.birth_date}")
        print(f"Khóa học: {student.course}")
        print(f"Khoa viện: {student.faculty}")
        print(f"Lớp: {student.class_name}")
        print(f"Ngành học: {student.major}")
        print("="*50)

    def display_all_students(self, show_gpa=False):
        """Hiển thị danh sách tất cả sinh viên"""
        if not self.students:
            print("Không có sinh viên nào trong hệ thống.")
            return
            
        print("\n" + "="*100)
        if show_gpa:
            print("{:<10} {:<25} {:<10} {:<15} {:<15} {:<10}".format(
                "MSSV", "Họ tên", "Giới tính", "Khóa học", "Khoa viện", "GPA"))
        else:
            print("{:<10} {:<25} {:<10} {:<15} {:<15}".format(
                "MSSV", "Họ tên", "Giới tính", "Khóa học", "Khoa viện"))
        print("="*100)
        
        for student in self.students:
            if show_gpa:
                print("{:<10} {:<25} {:<10} {:<15} {:<15} {:<10.2f}".format(
                    student.student_id, student.name, student.gender,
                    student.course, student.faculty, student.gpa))
            else:
                print("{:<10} {:<25} {:<10} {:<15} {:<15}".format(
                    student.student_id, student.name, student.gender,
                    student.course, student.faculty))
        print("="*100)

    def load_students_from_excel(self):
        """Đọc dữ liệu sinh viên từ file Excel"""
        self.students = ExcelFileHandler.load_from_excel(self.students_file, Student)

    def save_students_to_excel(self):
        """Lưu dữ liệu sinh viên vào file Excel"""
        headers = ['student_id', 'name', 'gender', 'birth_date', 'course', 'faculty', 'class_name', 'major']
        return ExcelFileHandler.save_to_excel(self.students_file, self.students, headers)

    def sort_by_name(self):
        """Sắp xếp sinh viên theo tên"""
        self.students.sort(key=lambda x: x.name.lower())

    def sort_by_gpa(self):
        """Sắp xếp sinh viên theo GPA"""
        self.students.sort(key=lambda x: x.gpa, reverse=True)

    def sort_by_id(self):
        """Sắp xếp sinh viên theo MSSV"""
        self.students.sort(key=lambda x: str(x.student_id))