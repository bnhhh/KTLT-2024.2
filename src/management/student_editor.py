from src.managers.student_manager import validate_date

def edit_student_info(system, student_id):
    """Xử lý quá trình chỉnh sửa thông tin sinh viên"""
    if not student_id:
        print("Vui lòng nhập MSSV.")
        return False

    # Kiểm tra sinh viên có tồn tại không
    student = system.student_manager.find_student_by_id(student_id)
    if not student:
        print("Không tìm thấy sinh viên!")
        return False

    new_info = {}
    
    # Xử lý nhập họ tên
    new_name = input(f"Họ tên: ").strip()
    if new_name: 
        is_valid, message = system.student_manager.validate_name(new_name)
        if not is_valid:
            print(f"Lỗi: {message}")
            return False
        new_info['name'] = new_name
    
    # Xử lý nhập ngày sinh
    new_birth_date = input(f"Ngày sinh (dd/mm/yyyy): ").strip()
    if new_birth_date:
        is_valid, message = validate_date(new_birth_date)
        if not is_valid:
            print(f"Lỗi: {message}")
            return False
        new_info['birth_date'] = new_birth_date
    
    # Xử lý nhập giới tính
    new_gender = input(f"Giới tính (Nam/Nữ): ").strip()
    if new_gender:
        is_valid, message = system.student_manager.validate_gender(new_gender)
        if not is_valid:
            print(f"Lỗi: {message}")
            return False
        new_info['gender'] = new_gender.capitalize()
    
    # Xử lý nhập ngành học
    new_major = input(f"Ngành học: ").strip()
    if new_major:
        is_valid, message = system.student_manager.validate_major(new_major)
        if not is_valid:
            print(f"Lỗi: {message}")
            return False
        new_info['major'] = new_major
    
    # Xử lý nhập khóa học
    new_course = input(f"Khóa học: ").strip()
    if new_course:
        is_valid, message = system.student_manager.validate_course(new_course)
        if not is_valid:
            print(f"Lỗi: {message}")
            return False
        new_info['course'] = new_course
    
    # Xử lý nhập khoa viện
    new_faculty = input(f"Khoa viện: ").strip()
    if new_faculty:
        is_valid, message = system.student_manager.validate_faculty(new_faculty)
        if not is_valid:
            print(f"Lỗi: {message}")
            return False
        new_info['faculty'] = new_faculty
    
    # Xử lý nhập lớp
    new_class = input(f"Lớp: ").strip()
    if new_class:
        is_valid, message = system.student_manager.validate_class_name(new_class)
        if not is_valid:
            print(f"Lỗi: {message}")
            return False
        new_info['class_name'] = new_class
    
    # Kiểm tra xem có thông tin nào được nhập không
    if not new_info:
        print("Không có thông tin nào được cập nhật.")
        return False

    # Kiểm tra xem có giá trị nào thực sự khác với giá trị hiện tại không
    has_changes = False
    for key, value in new_info.items():
        if getattr(student, key) != value:
            has_changes = True
            break

    if not has_changes:
        print("Không có thông tin nào được thay đổi.")
        return False

    # Thực hiện cập nhật
    return system.edit_student(student_id, new_info) 