"""
Module chính của hệ thống quản lý sinh viên.

Module này có các trách nhiệm chính:
1. Khởi tạo hệ thống quản lý sinh viên
2. Hiển thị và xử lý menu chính
3. Điều phối các chức năng quản lý sinh viên
4. Xử lý các trường hợp lỗi và ngoại lệ

"""

from management.management import StudentManagementSystem
from management.menu_handler import run_student_management, run_score_management, run_subject_management
from utils.menu_utils import MenuHandler

def main():
    """
    Hàm chính của chương trình.
    
    Chức năng:
    1. Khởi tạo hệ thống quản lý sinh viên
    2. Định nghĩa các tùy chọn menu chính
    3. Chạy menu thông qua MenuHandler
    4. Xử lý các trường hợp lỗi và ngoại lệ
    
    Xử lý ngoại lệ:
    - KeyboardInterrupt: Khi người dùng nhấn Ctrl+C
    - Exception: Các lỗi không mong muốn khác
    """
    try:
        # Khởi tạo hệ thống
        system = StudentManagementSystem()
        
        # Định nghĩa menu chính
        options = {
            '1': 'Quản lý sinh viên',
            '2': 'Quản lý điểm số',
            '3': 'Quản lý môn học',
            '10': 'Lưu dữ liệu',
            '0': 'Thoát chương trình'
        }
        
        # Định nghĩa các hàm xử lý
        handlers = {
            '1': lambda: run_student_management(system),
            '2': lambda: run_score_management(system),
            '3': lambda: run_subject_management(system),
            '10': lambda: system.save_data()
        }
        
        # Chạy menu chính
        MenuHandler.handle_menu("HỆ THỐNG QUẢN LÝ SINH VIÊN VÀ ĐIỂM SỐ", options, handlers)
        print("Cảm ơn đã sử dụng chương trình!")
        
    except KeyboardInterrupt:
        print("\nChương trình đã được kết thúc.")
    except Exception as e:
        print(f"\nLỗi không mong muốn: {str(e)}")
        print("Vui lòng kiểm tra lại dữ liệu và thử lại.")

if __name__ == "__main__":
    main() 