from management.management import StudentManagementSystem
from utils.menu_utils import MenuHandler
from management.menu_handler import run_student_management, run_score_management, run_subject_management

def main():
    """Khởi chạy chương trình quản lý sinh viên"""
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