from datetime import datetime

def validate_date(date_str):
    """Kiểm tra tính hợp lệ của ngày sinh"""
    if not date_str or not date_str.strip():
        return False, "Ngày sinh không được để trống"
    try:
        datetime.strptime(date_str, "%d/%m/%Y")
        return True, ""
    except ValueError:
        return False, "Ngày sinh phải có định dạng dd/mm/yyyy"

def is_valid_student_id(student_id):
    """Kiểm tra tính hợp lệ của mã số sinh viên"""
    if not student_id:  # Kiểm tra nếu student_id là None hoặc rỗng
        return False
    return student_id.isdigit() and len(student_id) == 8

def is_valid_name(name):
    """Kiểm tra tính hợp lệ của họ tên"""
    for char in name:
        if not ('a' <= char <= 'z' or 'A' <= char <= 'Z' or ' ' == char or 'À' <= char <= 'ỹ' or 'á' <= char <= 'ý' or 'Á' <= char <= 'Ý' or char in "ăâđêôơưĂÂĐÊÔƠƯ"):
            return False
    return True

def validate_student_id(student_id, existing_students=None, exclude_id=None):
    """Kiểm tra tính hợp lệ của mã số sinh viên"""
    if not student_id:
        return False, "MSSV không được để trống"
    if not is_valid_student_id(student_id):
        return False, "MSSV phải là 8 chữ số"
    if existing_students:
        for student in existing_students:
            if str(student.student_id) == str(student_id) and str(student_id) != str(exclude_id):
                return False, "MSSV đã tồn tại"
    return True, ""

def validate_name(name):
    """Kiểm tra tính hợp lệ của họ tên"""
    if not name or not name.strip():
        return False, "Họ tên không được để trống"
    if not is_valid_name(name):
        return False, "Họ tên không hợp lệ"
    return True, ""

def validate_gender(gender):
    """Kiểm tra tính hợp lệ của giới tính"""
    if not gender or not gender.strip():
        return False, "Giới tính không được để trống"
    if gender.lower() not in ['nam', 'nữ']:
        return False, "Giới tính phải là 'Nam' hoặc 'Nữ'"
    return True, ""

def validate_course(course):
    """Kiểm tra tính hợp lệ của khóa học"""
    if not course or not course.strip():
        return False, "Khóa học không được để trống"
    return True, ""

def validate_faculty(faculty):
    """Kiểm tra tính hợp lệ của khoa viện"""
    if not faculty or not faculty.strip():
        return False, "Khoa viện không được để trống"
    return True, ""

def validate_class_name(class_name):
    """Kiểm tra tính hợp lệ của lớp"""
    if not class_name or not class_name.strip():
        return False, "Lớp không được để trống"
    return True, ""

def validate_major(major):
    """Kiểm tra tính hợp lệ của ngành học"""
    if not major or not major.strip():
        return False, "Ngành học không được để trống"
    return True, ""

def validate_subject_code(subject_code, existing_subjects=None):
    """Kiểm tra tính hợp lệ của mã môn học"""
    if not subject_code or not subject_code.strip():
        return False, "Mã môn học không được để trống"
    if existing_subjects:
        for subject in existing_subjects:
            if subject.subject_code == subject_code:
                return False, "Mã môn học đã tồn tại"
    return True, ""

def validate_subject_name(subject_name):
    """Kiểm tra tính hợp lệ của tên môn học"""
    if not subject_name or not subject_name.strip():
        return False, "Tên môn học không được để trống"
    return True, ""

def validate_credits(credits_str):
    """Kiểm tra tính hợp lệ của số tín chỉ"""
    if not credits_str or not credits_str.strip():
        return False, "Số tín chỉ không được để trống"
    try:
        credits = int(credits_str)
        if credits <= 0:
            return False, "Số tín chỉ phải là số nguyên dương"
        return True, ""
    except ValueError:
        return False, "Số tín chỉ phải là số nguyên" 