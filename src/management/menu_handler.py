from src.core_types.student import Student
from src.managers.score_manager import validate_score, calculate_final_score, get_grade
from src.core_types.subject import Subject

def run_student_management(system):
    """Hàm chạy menu quản lý sinh viên"""
    while True:
        print("\n" + "="*50)
        print("                    QUẢN LÝ SINH VIÊN")
        print("="*50)
        print("1. Thêm sinh viên mới")
        print("2. Sửa thông tin sinh viên")
        print("3. Xóa sinh viên")
        print("4. Tìm kiếm sinh viên")
        print("5. Hiển thị tất cả sinh viên")
        print("6. Xem điểm trung bình (GPA) và xếp loại")
        print("7. Sắp xếp danh sách sinh viên")
        print("0. Quay lại menu chính")
        print("="*50)
        choice = input("Chọn chức năng: ").strip()

        if choice == '1':
            print("\n=== THÊM SINH VIÊN MỚI ===")
            student_id = input("Nhập MSSV (8 chữ số): ").strip()
            name = input("Nhập họ tên: ").strip()
            birth_date = input("Nhập ngày sinh (dd/mm/yyyy): ").strip()
            gender = input("Nhập giới tính (Nam/Nữ): ").strip()
            major = input("Nhập ngành học: ").strip()
            course = input("Nhập khóa học: ").strip()
            faculty = input("Nhập khoa viện: ").strip()
            class_name = input("Nhập lớp: ").strip()
            student = Student(student_id, name, birth_date, major, gender, course, faculty, class_name)
            system.add_student(student)
        elif choice == '2':
            print("\n=== SỬA THÔNG TIN SINH VIÊN ===")
            student_id = input("Nhập MSSV cần sửa: ").strip()
            if student_id:
                new_info = {}
                new_name = input(f"Họ tên: ").strip()
                if new_name: new_info['name'] = new_name
                new_birth_date = input(f"Ngày sinh (dd/mm/yyyy): ").strip()
                if new_birth_date: new_info['birth_date'] = new_birth_date
                new_gender = input(f"Giới tính (Nam/Nữ): ").strip()
                if new_gender: new_info['gender'] = new_gender.capitalize()
                new_major = input(f"Ngành học: ").strip()
                if new_major: new_info['major'] = new_major
                new_course = input(f"Khóa học: ").strip()
                if new_course: new_info['course'] = new_course
                new_faculty = input(f"Khoa viện: ").strip()
                if new_faculty: new_info['faculty'] = new_faculty
                new_class = input(f"Lớp: ").strip()
                if new_class: new_info['class_name'] = new_class
                system.edit_student(student_id, new_info)
            else:
                print("Vui lòng nhập MSSV.")
        elif choice == '3':
            print("\n=== XÓA SINH VIÊN ===")
            student_id = input("Nhập MSSV cần xóa: ").strip()
            system.student_manager.delete_student(student_id)
        elif choice == '4':
            print("\n=== TÌM KIẾM SINH VIÊN ===")
            print("1. Tìm theo MSSV")
            print("2. Tìm theo họ tên")
            print("3. Tìm theo lớp")
            print("4. Tìm theo khoa")
            search_type = input("Chọn cách tìm kiếm: ").strip()
            keyword = input("Nhập từ khóa: ").strip()
            results = system.student_manager.search_students(search_type, keyword)
            if results:
                print("\nKết quả tìm kiếm:")
                for student in results:
                    system.student_manager.display_student_info(student)
            else:
                print("Không tìm thấy sinh viên nào.")
        elif choice == '5':
            system.student_manager.display_all_students()
        elif choice == '6':
            print("\n=== XEM ĐIỂM TRUNG BÌNH (GPA) VÀ XẾP LOẠI ===")
            # Cập nhật lại thông tin điểm số cho sinh viên trước khi tính GPA
            for student in system.student_manager.students:
                student.scores = {}  # Reset điểm số cũ
                for score_data in system.score_manager.scores:
                    student_id = str(int(score_data['student_id'])) if isinstance(score_data['student_id'],
                                                                                  float) else str(
                        score_data['student_id'])
                    if student.student_id == student_id:
                        subject_code = score_data['subject_code']
                        score = score_data['total_score']
                        student.add_score(subject_code, score)

            for student in system.student_manager.students:
                student.calculate_gpa(system)
                student.assign_grade()
            system.student_manager.display_all_students(show_gpa=True)
        elif choice == '7':
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

            system.student_manager.display_all_students(show_gpa=sort_choice == '2')

        elif choice == '0':
            break
        else:
            print("Lựa chọn không hợp lệ!")

        input("\nNhấn Enter để tiếp tục...")

def run_score_management(system):
    """Hàm chạy menu quản lý điểm số"""
    while True:
        print("\n" + "="*50)
        print("                    QUẢN LÝ ĐIỂM SỐ")
        print("="*50)
        print("1. Nhập điểm cho sinh viên")
        print("2. Sửa điểm sinh viên")
        print("3. Xóa điểm")
        print("4. Xem điểm sinh viên")
        print("0. Quay lại menu chính")
        print("="*50)
        choice = input("Chọn chức năng: ").strip()

        if choice == '1':
            print("\n=== NHẬP ĐIỂM CHO SINH VIÊN ===")
            student_id = input("Nhập MSSV: ").strip()
            subject_code = input("Nhập mã học phần: ").strip()
            attendance_str = input("Nhập điểm chuyên cần (0-10): ").strip()
            midterm_str = input("Nhập điểm giữa kỳ (0-10): ").strip()
            final_str = input("Nhập điểm cuối kỳ (0-10): ").strip()

            valid_cc = validate_score(attendance_str)
            valid_gk = validate_score(midterm_str)
            valid_ck = validate_score(final_str)

            if valid_cc[0] and valid_gk[0] and valid_ck[0]:
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
            else:
                print("Lỗi nhập điểm. Vui lòng kiểm tra lại.")
        elif choice == '2':
            print("\n=== SỬA ĐIỂM SINH VIÊN ===")
            student_id = input("Nhập MSSV: ").strip()
            subject_code = input("Nhập mã học phần: ").strip()
            new_scores = {}
            new_attendance = input("Nhập điểm chuyên cần mới (hoặc Enter để bỏ qua): ").strip()
            if new_attendance:
                if validate_score(new_attendance)[0]:
                    new_scores['attendance_score'] = float(new_attendance)
                else:
                    print("Điểm chuyên cần không hợp lệ.")
            new_midterm = input("Nhập điểm giữa kỳ mới (hoặc Enter để bỏ qua): ").strip()
            if new_midterm:
                if validate_score(new_midterm)[0]:
                    new_scores['midterm_score'] = float(new_midterm)
                else:
                    print("Điểm giữa kỳ không hợp lệ.")
            new_final = input("Nhập điểm cuối kỳ mới (hoặc Enter để bỏ qua): ").strip()
            if new_final:
                if validate_score(new_final)[0]:
                    new_scores['final_score'] = float(new_final)
                else:
                    print("Điểm cuối kỳ không hợp lệ.")
            if new_scores:
                student_scores = system.score_manager.find_score_record(student_id, subject_code).copy() if system.score_manager.find_score_record(student_id, subject_code) else {}
                attendance = new_scores.get('attendance_score', student_scores.get('attendance_score', 0.0))
                midterm = new_scores.get('midterm_score', student_scores.get('midterm_score', 0.0))
                final = new_scores.get('final_score', student_scores.get('final_score', 0.0))
                total_score = calculate_final_score(attendance, midterm, final)
                new_scores['total_score'] = round(total_score, 2)
                new_scores['grade'] = get_grade(total_score)
                system.score_manager.edit_score(student_id, subject_code, new_scores)
        elif choice == '3':
            print("\n=== XÓA ĐIỂM ===")
            student_id = input("Nhập MSSV: ").strip()
            subject_code = input("Nhập mã học phần: ").strip()
            system.score_manager.delete_score(student_id, subject_code)
        elif choice == '4':
            print("\n=== XEM ĐIỂM SINH VIÊN ===")
            print("1. Xem điểm của một sinh viên (tất cả môn)")
            print("2. Xem điểm một môn của tất cả sinh viên")
            view_choice = input("Chọn cách xem điểm: ").strip()
            if view_choice == '1':
                student_id = input("Nhập MSSV: ").strip()
                system.score_manager.view_student_scores(student_id, system.student_manager.students)
            elif view_choice == '2':
                subject_code = input("Nhập mã học phần: ").strip()
                system.score_manager.view_subject_scores(subject_code, system.student_manager.students)
            else:
                print("Lựa chọn không hợp lệ!")
        elif choice == '0':
            break
        else:
            print("Lựa chọn không hợp lệ!")

        input("\nNhấn Enter để tiếp tục...")

def run_subject_management(system):
    """Hàm chạy menu quản lý môn học"""
    while True:
        print("\n" + "="*50)
        print("                    QUẢN LÝ MÔN HỌC")
        print("="*50)
        print("1. Thêm môn học mới")
        print("2. Sửa thông tin môn học")
        print("3. Xóa môn học")
        print("4. Xem tất cả môn học")
        print("0. Quay lại menu chính")
        print("="*50)
        choice = input("Chọn chức năng: ").strip()

        if choice == '1':
            print("\n=== THÊM MÔN HỌC MỚI ===")
            subject_code = input("Nhập mã môn học: ").strip()
            is_valid, message = system.subject_manager.validate_subject_code(subject_code)
            if not is_valid:
                print(message)
                continue
            subject_name = input("Nhập tên môn học: ").strip()
            is_valid, message = system.subject_manager.validate_subject_name(subject_name)
            if not is_valid:
                print(message)
                continue
            while True:
                credits_str = input("Nhập số tín chỉ: ").strip()
                try:
                    credits = int(credits_str)
                    if credits > 0:
                        break
                    else:
                        print("Số tín chỉ phải là số nguyên dương.")
                except ValueError:
                    print("Vui lòng nhập một số nguyên hợp lệ.")
            subject = Subject(subject_code, subject_name, credits)
            system.subject_manager.add_subject(subject)
        elif choice == '2':
            print("\n=== SỬA THÔNG TIN MÔN HỌC ===")
            subject_code_to_edit = input("Nhập mã môn học cần sửa: ").strip()
            subject_to_edit = system.subject_manager.find_subject_by_code(subject_code_to_edit)
            if subject_to_edit:
                new_info = {}
                new_name = input(f"Tên môn học mới (ấn Enter để bỏ qua): ").strip()
                if new_name:
                    new_info['subject_name'] = new_name
                new_credits_str = input(f"Số tín chỉ mới (ấn Enter để bỏ qua): ").strip()
                if new_credits_str:
                    try:
                        new_credits = int(new_credits_str)
                        if new_credits > 0:
                            new_info['credits'] = new_credits
                        else:
                            print("Số tín chỉ phải là số nguyên dương.")
                    except ValueError:
                        print("Vui lòng nhập một số nguyên hợp lệ cho số tín chỉ.")
                if new_info:
                    system.subject_manager.edit_subject(subject_code_to_edit, new_info)
            else:
                print("Không tìm thấy môn học!")
        elif choice == '3':
            print("\n=== XÓA MÔN HỌC ===")
            subject_code_to_delete = input("Nhập mã môn học cần xóa: ").strip()
            system.subject_manager.delete_subject(subject_code_to_delete)
        elif choice == '4':
            system.subject_manager.display_all_subjects()
        elif choice == '0':
            break
        else:
            print("Lựa chọn không hợp lệ!")
        input("\nNhấn Enter để tiếp tục...")