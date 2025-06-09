"""
Module Xử lý Menu

Module này chứa các hàm xử lý giao diện dòng lệnh và menu cho hệ thống quản lý sinh viên.
Các hàm được tách riêng để dễ dàng bảo trì và mở rộng.

Các chức năng chính:
- Quản lý sinh viên: Thêm, sửa, xóa, tìm kiếm, hiển thị, xem GPA, sắp xếp
- Quản lý điểm số: Thêm, sửa, xóa điểm
- Quản lý môn học: Thêm, sửa, xóa môn học, hiển thị, tìm kiếm
"""

from core_types.student import Student
from utils.score_utils import validate_score, calculate_final_score, get_grade
from core_types.subject import Subject
from utils.menu_utils import MenuHandler
from utils.validation_utils import validate_subject_code, validate_subject_name, validate_credits

def edit_student_info(student):
    """
    Chỉnh sửa thông tin sinh viên thông qua nhập liệu từ người dùng.
    
    Tham số đầu vào:
        student (Student): Đối tượng sinh viên cần chỉnh sửa
        
    Trả về:
        bool: True nếu chỉnh sửa thành công, False nếu thất bại
    """
    print("\n=== CHỈNH SỬA THÔNG TIN SINH VIÊN ===")
    print("Nhập thông tin mới (để trống nếu không muốn thay đổi):")
    new_info = {}
    # Nhập và kiểm tra họ tên
    new_name = input("Họ tên: ").strip()
    if new_name:
        new_info['name'] = new_name
        
    new_birth_date = input(f"Ngày sinh mới [{student.birth_date}]: ").strip()
    if new_birth_date:
        new_info['birth_date'] = new_birth_date
        
    new_gender = input(f"Giới tính mới [{student.gender}]: ").strip()
    if new_gender:
        new_info['gender'] = new_gender
        
    new_course = input(f"Khóa học mới [{student.course}]: ").strip()
    if new_course:
        new_info['course'] = new_course
        
    new_faculty = input(f"Khoa viện mới [{student.faculty}]: ").strip()
    if new_faculty:
        new_info['faculty'] = new_faculty
        
    new_class = input(f"Lớp mới [{student.class_name}]: ").strip()
    if new_class:
        new_info['class_name'] = new_class
        
    new_major = input(f"Ngành học mới [{student.major}]: ").strip()
    if new_major:
        new_info['major'] = new_major
        
    return new_info if new_info else None

def run_student_management(system):
    """
    Chạy menu quản lý sinh viên.
    
    Tham số đầu vào:
        system (StudentManagementSystem): Hệ thống quản lý sinh viên
    """
    options = {
        '1': 'Thêm sinh viên mới',
        '2': 'Sửa thông tin sinh viên',
        '3': 'Xóa sinh viên',
        '4': 'Tìm kiếm sinh viên',
        '5': 'Hiển thị tất cả sinh viên',
        '6': 'Xem điểm trung bình (GPA) và xếp loại',
        '7': 'Sắp xếp danh sách sinh viên',
        '0': 'Quay lại menu chính'
    }
    
    handlers = {
        '1': lambda: handle_add_student(system),
        '2': lambda: handle_edit_student(system),
        '3': lambda: handle_delete_student(system),
        '4': lambda: handle_search_student(system),
        '5': lambda: system.student_manager.display_all_students(),
        '6': lambda: handle_view_gpa(system),
        '7': lambda: handle_sort_students(system)
    }
    
    MenuHandler.handle_menu("QUẢN LÝ SINH VIÊN", options, handlers)

def handle_add_student(system):
    """
    Thêm sinh viên mới.
    
    Tham số đầu vào:
        system (StudentManagementSystem): Hệ thống quản lý sinh viên
    """
    print("\n=== THÊM SINH VIÊN MỚI ===")
    student_id = input("Nhập MSSV: ").strip()
    name = input("Nhập họ tên: ").strip()
    birth_date = input("Nhập ngày sinh (dd/mm/yyyy): ").strip()
    gender = input("Nhập giới tính: ").strip()
    course = input("Nhập khóa học: ").strip()
    faculty = input("Nhập khoa viện: ").strip()
    class_name = input("Nhập lớp: ").strip()
    major = input("Nhập ngành học: ").strip()
    
    student = Student(student_id, name, birth_date, major, gender, course, faculty, class_name)
    system.add_student(student)

def handle_edit_student(system):
    """
    Sửa thông tin sinh viên.
    
    Tham số đầu vào:
        system (StudentManagementSystem): Hệ thống quản lý sinh viên
    """
    print("\n=== SỬA THÔNG TIN SINH VIÊN ===")
    student_id = input("Nhập MSSV cần sửa: ").strip()
    student = system.student_manager.find_student_by_id(student_id)
    if student:
        new_info = edit_student_info(student)
        if new_info:
            system.edit_student(student_id, new_info)
    else:
        print("Không tìm thấy sinh viên!")

def handle_delete_student(system):
    """
    Xóa sinh viên.
    
    Tham số đầu vào:
        system (StudentManagementSystem): Hệ thống quản lý sinh viên
    """
    print("\n=== XÓA SINH VIÊN ===")
    student_id = input("Nhập MSSV cần xóa: ").strip()
    system.student_manager.delete_student(student_id)

def handle_search_student(system):
    """
    Tìm kiếm sinh viên.
    
    Tham số đầu vào:
        system (StudentManagementSystem): Hệ thống quản lý sinh viên
    """
    print("\n=== TÌM KIẾM SINH VIÊN ===")
    print("1. Theo MSSV")
    print("2. Theo tên")
    print("3. Theo lớp")
    print("4. Theo khoa")
    search_type = input("Chọn cách tìm kiếm: ").strip()
    keyword = input("Nhập từ khóa tìm kiếm: ").strip()
    
    results = system.student_manager.search_students(search_type, keyword)
    if results:
        print("\n" + "="*100)
        print("{:<10} {:<25} {:<10} {:<15} {:<15}".format(
            "MSSV", "Họ tên", "Giới tính", "Khóa học", "Khoa viện"))
        print("="*100)
        for student in results:
            print("{:<10} {:<25} {:<10} {:<15} {:<15}".format(
                student.student_id, student.name, student.gender,
                student.course, student.faculty))
        print("="*100)

def handle_view_gpa(system):
    """
    Xem điểm trung bình (GPA) và xếp loại.
    
    Tham số đầu vào:
        system (StudentManagementSystem): Hệ thống quản lý sinh viên
    """
    print("\n=== XEM ĐIỂM TRUNG BÌNH (GPA) VÀ XẾP LOẠI ===")
    for student in system.student_manager.students:
        student.scores = {}
        for score_data in system.score_manager.scores:
            student_id = str(int(score_data['student_id'])) if isinstance(score_data['student_id'], float) else str(score_data['student_id'])
            if student.student_id == student_id:
                subject_code = score_data['subject_code']
                score = score_data['total_score']
                student.add_score(subject_code, score)
        student.calculate_gpa(system)
    system.student_manager.display_all_students(show_gpa=True)

def handle_sort_students(system):
    """
    Sắp xếp danh sách sinh viên.
    
    Tham số đầu vào:
        system (StudentManagementSystem): Hệ thống quản lý sinh viên
    """
    print("\n=== SẮP XẾP DANH SÁCH SINH VIÊN ===")
    print("1. Theo tên")
    print("2. Theo điểm trung bình (GPA)")
    print("3. Theo MSSV")
    sort_choice = input("Chọn cách sắp xếp: ").strip()
    
    if sort_choice == '1':
        system.student_manager.sort_by_name()
    elif sort_choice == '2':
        for student in system.student_manager.students:
            student.calculate_gpa(system)
        system.student_manager.sort_by_gpa()
    elif sort_choice == '3':
        system.student_manager.sort_by_id()
    else:
        print("Lựa chọn không hợp lệ.")
        return
        
    system.student_manager.display_all_students(show_gpa=sort_choice == '2')

def run_score_management(system):
    """
    Chạy menu quản lý điểm số.
    
    Tham số đầu vào:
        system (StudentManagementSystem): Hệ thống quản lý sinh viên
    """
    options = {
        '1': 'Thêm điểm',
        '2': 'Sửa điểm',
        '3': 'Xóa điểm',
        '4': 'Xem điểm số',
        '0': 'Quay lại menu chính'
    }
    
    handlers = {
        '1': lambda: handle_add_score(system),
        '2': lambda: handle_edit_score(system),
        '3': lambda: handle_delete_score(system),
        '4': lambda: handle_view_scores(system)
    }
    
    MenuHandler.handle_menu("QUẢN LÝ ĐIỂM SỐ", options, handlers)

def handle_add_score(system):
    """
    Nhập điểm cho sinh viên.
    
    Tham số đầu vào:
        system (StudentManagementSystem): Hệ thống quản lý sinh viên
    """
    print("\n=== NHẬP ĐIỂM ===")
    student_id = input("Nhập MSSV: ").strip()
    subject_code = input("Nhập mã học phần: ").strip()
    
    if not system.student_manager.find_student_by_id(student_id):
        print("Không tìm thấy sinh viên!")
        return
    
    # Kiểm tra mã học phần có tồn tại không
    subject = next((s for s in system.subject_manager.subjects if s.subject_code == subject_code), None)
    if not subject:
        print("Mã học phần không tồn tại!")
        return
        
    attendance_str = input("Nhập điểm chuyên cần: ").strip()
    midterm_str = input("Nhập điểm giữa kỳ: ").strip()
    final_str = input("Nhập điểm cuối kỳ: ").strip()
    
    valid_cc = validate_score(attendance_str)
    valid_gk = validate_score(midterm_str)
    valid_ck = validate_score(final_str)
    
    if not all([valid_cc[0], valid_gk[0], valid_ck[0]]):
        print("Lỗi nhập điểm. Vui lòng kiểm tra lại.")
        return
        
    attendance = float(attendance_str)
    midterm = float(midterm_str)
    final = float(final_str)
    total_score = calculate_final_score(attendance, midterm, final)
    grade = get_grade(total_score)
    
    score_record = {
        'student_id': student_id,
        'subject_code': subject_code,
        'attendance_score': attendance,
        'midterm_score': midterm,
        'final_score': final,
        'total_score': round(total_score, 2),
        'grade': grade
    }
    system.score_manager.add_score(score_record)

    # Cập nhật điểm và tính lại GPA cho sinh viên
    student = system.student_manager.find_student_by_id(student_id)
    if student:
        student.scores = {}
        for score_data in system.score_manager.scores:
            if score_data['student_id'] == student_id:
                subj_code = score_data['subject_code']
                score = score_data['total_score']
                student.add_score(subj_code, score)
        student.calculate_gpa(system)
        print(f"GPA mới của sinh viên {student.student_id}: {student.gpa:.2f}")
        print(f"Xếp loại mới: {student.grade}")

def handle_edit_score(system):
    """
    Sửa điểm của sinh viên.
    
    Tham số đầu vào:
        system (StudentManagementSystem): Hệ thống quản lý sinh viên
    """
    print("\n=== SỬA ĐIỂM ===")
    student_id = input("Nhập MSSV: ").strip()
    subject_code = input("Nhập mã học phần: ").strip()
    
    if not system.student_manager.find_student_by_id(student_id):
        print("Không tìm thấy sinh viên!")
        return
    
    # Kiểm tra mã học phần có tồn tại không
    subject = next((s for s in system.subject_manager.subjects if s.subject_code == subject_code), None)
    if not subject:
        print("Mã học phần không tồn tại!")
        return
    
    new_scores = {}
    attendance_str = input("Điểm chuyên cần mới (ấn Enter để bỏ qua): ").strip()
    if attendance_str:
        valid, message = validate_score(attendance_str)
        if valid:
            new_scores['attendance_score'] = float(attendance_str)
        else:
            print(message)
            return
            
    midterm_str = input("Điểm giữa kỳ mới (ấn Enter để bỏ qua): ").strip()
    if midterm_str:
        valid, message = validate_score(midterm_str)
        if valid:
            new_scores['midterm_score'] = float(midterm_str)
        else:
            print(message)
            return
            
    final_str = input("Điểm cuối kỳ mới (ấn Enter để bỏ qua): ").strip()
    if final_str:
        valid, message = validate_score(final_str)
        if valid:
            new_scores['final_score'] = float(final_str)
        else:
            print(message)
            return
            
    if new_scores:
        system.score_manager.edit_score(student_id, subject_code, new_scores)
        print("✓ Cập nhật điểm thành công!")
    else:
        print("Không có thay đổi nào được thực hiện.")

def handle_delete_score(system):
    """
    Xóa điểm của sinh viên.

    Tham số đầu vào:
        system (StudentManagementSystem): Hệ thống quản lý sinh viên
    """
    print("\n=== XÓA ĐIỂM ===")
    student_id = input("Nhập MSSV: ").strip()
    subject_code = input("Nhập mã học phần: ").strip()
    system.score_manager.delete_score(student_id, subject_code)

def handle_view_scores(system):
    """
    Xem điểm số của sinh viên.

    Tham số đầu vào:
        system (StudentManagementSystem): Hệ thống quản lý sinh viên
    """
    print("\n=== XEM ĐIỂM SỐ ===")
    print("1. Xem điểm của một sinh viên")
    print("2. Xem điểm một môn của tất cả sinh viên")
    choice = input("Chọn cách xem điểm: ").strip()

    if choice == '1':
        student_id = input("Nhập MSSV: ").strip()
        system.score_manager.view_student_scores(student_id, system.student_manager.students)
    elif choice == '2':
        subject_code = input("Nhập mã học phần: ").strip()
        # Kiểm tra mã học phần có tồn tại không
        subject = next((s for s in system.subject_manager.subjects if s.subject_code == subject_code), None)
        if not subject:
            print("Mã học phần không tồn tại!")
            return
        system.score_manager.view_subject_scores(subject_code, system.student_manager.students)
    else:
        print("Lựa chọn không hợp lệ.")

def run_subject_management(system):
    """
    Chạy menu quản lý môn học.
    
    Tham số đầu vào:
        system (StudentManagementSystem): Hệ thống quản lý sinh viên
    """
    options = {
        '1': 'Thêm môn học',
        '2': 'Sửa môn học',
        '3': 'Xóa môn học',
        '4': 'Hiển thị tất cả môn học',
        '5': 'Tìm kiếm môn học',
        '0': 'Quay lại menu chính'
    }
    
    handlers = {
        '1': lambda: handle_add_subject(system),
        '2': lambda: handle_edit_subject(system),
        '3': lambda: handle_delete_subject(system),
        '4': lambda: system.subject_manager.display_all_subjects(),
        '5': lambda: handle_search_subject(system)
    }
    
    MenuHandler.handle_menu("QUẢN LÝ MÔN HỌC", options, handlers)

def handle_add_subject(system):
    """
    Thêm môn học mới.
    
    Tham số đầu vào:
        system (StudentManagementSystem): Hệ thống quản lý sinh viên
    """
    print("\n=== THÊM MÔN HỌC MỚI ===")
    subject_code = input("Nhập mã môn học: ").strip()
    subject_name = input("Nhập tên môn học: ").strip()
    credits_str = input("Nhập số tín chỉ: ").strip()
    
    valid_code, code_message = validate_subject_code(subject_code, system.subject_manager.subjects)
    if not valid_code:
        print(code_message)
        return
        
    valid_name, name_message = validate_subject_name(subject_name)
    if not valid_name:
        print(name_message)
        return
        
    valid_credits, credits_message = validate_credits(credits_str)
    if not valid_credits:
        print(credits_message)
        return
        
    subject = Subject(subject_code, subject_name, int(credits_str))
    system.add_subject(subject)

def handle_edit_subject(system):
    """
    Sửa thông tin môn học.
    
    Tham số đầu vào:
        system (StudentManagementSystem): Hệ thống quản lý sinh viên
    """
    print("\n=== SỬA THÔNG TIN MÔN HỌC ===")
    subject_code = input("Nhập mã môn học cần sửa: ").strip()
    subject = next((s for s in system.subject_manager.subjects if s.subject_code == subject_code), None)
    
    if not subject:
        print("Không tìm thấy môn học!")
        return
        
    print("\nNhập thông tin mới (ấn Enter để bỏ qua):")
    new_name = input(f"Tên môn học mới [{subject.subject_name}]: ").strip()
    new_credits = input(f"Số tín chỉ mới [{subject.credits}]: ").strip()
    
    new_info = {}
    if new_name:
        valid, message = validate_subject_name(new_name)
        if valid:
            new_info['subject_name'] = new_name
        else:
            print(message)
            return
            
    if new_credits:
        valid, message = validate_credits(new_credits)
        if valid:
            new_info['credits'] = int(new_credits)
        else:
            print(message)
            return
            
    if new_info:
        system.subject_manager.edit_subject(subject_code, new_info)
    else:
        print("Không có thay đổi nào được thực hiện.")

def handle_delete_subject(system):
    """
    Xóa môn học.
    
    Tham số đầu vào:
        system (StudentManagementSystem): Hệ thống quản lý sinh viên
    """
    print("\n=== XÓA MÔN HỌC ===")
    subject_code = input("Nhập mã môn học cần xóa: ").strip()
    system.subject_manager.delete_subject(subject_code)


def handle_search_subject(system):
    """
    Tìm kiếm môn học.

    Tham số đầu vào:
        system (StudentManagementSystem): Hệ thống quản lý sinh viên
    """
    print("\n=== TÌM KIẾM MÔN HỌC ===")
    print("1. Theo mã môn học")
    print("2. Theo tên môn học")
    search_type = input("Chọn cách tìm kiếm: ").strip()
    keyword = input("Nhập từ khóa tìm kiếm: ").strip()

    found_subjects = []
    if search_type == '1':
        # Sử dụng find_subject_by_code cho tìm kiếm chính xác
        subject = system.subject_manager.find_subject_by_code(keyword)
        if subject:
            found_subjects = [subject]
        # Tìm kiếm một phần nếu không tìm thấy kết quả chính xác
        if not found_subjects:
            found_subjects = [s for s in system.subject_manager.subjects if keyword.lower() in s.subject_code.lower()]
    elif search_type == '2':
        found_subjects = [s for s in system.subject_manager.subjects if keyword.lower() in s.subject_name.lower()]
    else:
        print("Lựa chọn không hợp lệ!")
        return

    if found_subjects:
        print("\n" + "=" * 50)
        print("{:<15} {:<30} {:<10}".format("Mã môn học", "Tên môn học", "Tín chỉ"))
        print("=" * 50)
        for subject in found_subjects:
            print("{:<15} {:<30} {:<10}".format(subject.subject_code, subject.subject_name, subject.credits))
        print("=" * 50)
    else:
        print("Không tìm thấy môn học nào!")