from core_types.student import Student
from utils.file_utils import ExcelFileHandler
from utils.validation_utils import (
    validate_date, validate_student_id, validate_name, validate_gender,
    validate_course, validate_faculty, validate_class_name, validate_major
)

class StudentManager:
    def __init__(self, students_data=None, students_file="students.xlsx"):
        self.students = students_data if students_data is not None else []
        self.students_file = students_file

    def find_student_by_id(self, student_id):
        """Tìm kiếm sinh viên theo mã số sinh viên"""
        for student in self.students:
            if str(student.student_id) == student_id:
                return student
        return None

    def add_student(self, student):
        """Thêm sinh viên mới vào hệ thống"""
        # Kiểm tra tính hợp lệ của tất cả các trường
        is_valid_id, id_message = validate_student_id(student.student_id, existing_students=self.students)
        if not is_valid_id:
            print(f"Lỗi: {id_message}")
            return False

        # Kiểm tra các trường còn lại
        validations = [
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
            is_valid_id, message = validate_student_id(new_student_id, existing_students=self.students, exclude_id=student_id)
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
                results = [s for s in self.students if keyword == str(s.student_id).lower()]
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
            print("{:<10} {:<25} {:<10} {:<15} {:<15} {:<10} {:<10}".format(
                "MSSV", "Họ tên", "Giới tính", "Khóa học", "Khoa viện", "GPA", "Xếp loại"))
        else:
            print("{:<10} {:<25} {:<10} {:<15} {:<15}".format(
                "MSSV", "Họ tên", "Giới tính", "Khóa học", "Khoa viện"))
        print("="*100)
        
        for student in self.students:
            if show_gpa:
                print("{:<10} {:<25} {:<10} {:<15} {:<15} {:<10.2f} {:<10}".format(
                    student.student_id, student.name, student.gender,
                    student.course, student.faculty, student.gpa, student.grade))
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
        """Sắp xếp sinh viên theo tên (ưu tiên tên gọi, sau đó đến họ và tên đệm)"""
        def name_key(student):
            parts = student.name.strip().split()
            return (parts[-1].lower(), " ".join(parts[:-1]).lower())
        self.students.sort(key=name_key)

    def sort_by_gpa(self):
        """Sắp xếp sinh viên theo GPA"""
        self.students.sort(key=lambda x: x.gpa, reverse=True)

    def sort_by_id(self):
        """Sắp xếp sinh viên theo MSSV"""
        self.students.sort(key=lambda x: str(x.student_id))