# Hệ Thống Quản Lý Sinh Viên và Điểm Số

## Mô tả
Chương trình này là một hệ thống quản lý thông tin sinh viên và điểm số được xây dựng bằng Python. Nó cho phép người dùng thực hiện các thao tác cơ bản như thêm, sửa, xóa, tìm kiếm sinh viên, quản lý điểm số cho từng môn học, quản lý danh sách môn học, tính toán điểm trung bình (GPA) và xếp loại học lực. Dữ liệu được lưu trữ và đọc từ các file Excel.

## Chức năng chính
* **Quản lý Sinh viên:**
    * Thêm sinh viên mới (MSSV, họ tên, ngày sinh, giới tính, ngành học, khóa học, khoa viện, lớp).
    * Sửa thông tin sinh viên.
    * Xóa sinh viên.
    * Tìm kiếm sinh viên theo MSSV, họ tên, lớp, khoa.
    * Hiển thị danh sách tất cả sinh viên.
    * Xem điểm trung bình (GPA) và xếp loại học lực cho tất cả sinh viên.
    * Sắp xếp danh sách sinh viên theo tên, GPA, hoặc MSSV.
* **Quản lý Điểm số:**
    * Nhập điểm chuyên cần, giữa kỳ, cuối kỳ cho sinh viên theo mã học phần.
    * Sửa điểm của sinh viên cho một môn học cụ thể.
    * Xóa điểm của sinh viên cho một môn học.
    * Xem bảng điểm của một sinh viên.
    * Xem bảng điểm của một môn học cho tất cả sinh viên.
* **Quản lý Môn học:**
    * Thêm môn học mới (mã môn, tên môn, số tín chỉ).
    * Sửa thông tin môn học.
    * Xóa môn học.
    * Xem danh sách tất cả môn học.
* **Lưu trữ dữ liệu:** Tất cả dữ liệu (sinh viên, điểm số, môn học) được lưu trữ vào các file Excel (`students.xlsx`, `scores.xlsx`, `subjects.xlsx`).

## Cấu trúc chương trình

KTLT-2024.2/
├── main.py
├── README.txt
├── scores.xlsx
├── students.xlsx
├── subjects.xlsx
└── src/
    ├── __init__.py
    ├── core_types/
    │   ├── student.py
    │   └── subject.py
    ├── management/
    │   ├── management.py
    │   └── menu_handler.py
    └── managers/
        ├── score_manager.py
        ├── student_manager.py
        └── subject_manager.py

Chương trình được chia thành các file Python sau:
* `student.py`: Định nghĩa class `Student` để biểu diễn thông tin của một sinh viên (ID, tên, ngày sinh, điểm số...).
* `student_manager.py`: Định nghĩa class `StudentManager` để quản lý danh sách sinh viên (thêm, sửa, xóa, tìm kiếm, hiển thị, sắp xếp, load và save dữ liệu sinh viên từ file Excel).
* `score_manager.py`: Định nghĩa class `ScoreManager` để quản lý điểm số của sinh viên (thêm, sửa, xóa, xem điểm, load và save dữ liệu điểm số từ file Excel).
* `subject.py`: Định nghĩa class `Subject` để biểu diễn thông tin của một môn học (mã môn, tên môn, số tín chỉ).
* `subject_manager.py`: Định nghĩa class `SubjectManager` để quản lý danh sách môn học (thêm, sửa, xóa, hiển thị, load và save dữ liệu môn học từ file Excel).
* `menu_handler.py`: Chứa các hàm để xử lý menu cho từng chức năng chính của chương trình (`run_student_management`, `run_score_management`, `run_subject_management`).
* `student_management.py`: Chứa class `StudentManagementSystem`, là lớp trung tâm để khởi tạo và quản lý toàn bộ hệ thống, điều phối hoạt động giữa các manager, và chứa hàm `run` cho menu chính.
* `main.py`: File chính để chạy chương trình, tạo instance của `StudentManagementSystem` và gọi phương thức `run` để bắt đầu chương trình.

## Yêu cầu
* Python 3.x đã được cài đặt trên máy tính.
* Thư viện `openpyxl` cần được cài đặt để làm việc với file Excel. Bạn có thể cài đặt bằng lệnh:
    ```bash
    pip install openpyxl
    ```

## Hướng dẫn cài đặt
1.  Sao chép hoặc tải xuống tất cả các file Python (`student.py`, `student_manager.py`, `score_manager.py`, `subject.py`, `subject_manager.py`, `menu_handler.py`, `student_management.py`, `main.py`) vào cùng một thư mục.
2.  Đảm bảo bạn đã cài đặt thư viện `openpyxl` như đã hướng dẫn ở trên.

## Hướng dẫn sử dụng
1.  Mở terminal hoặc command prompt, điều hướng đến thư mục chứa các file chương trình.
2.  Chạy chương trình bằng lệnh:
    ```bash
    python main.py
    ```
3.  Menu chính của chương trình sẽ hiển thị. Bạn có thể chọn các chức năng bằng cách nhập số tương ứng:
    * `1`: Quản lý sinh viên (Thêm, Sửa, Xóa, Tìm kiếm, Hiển thị, Xem GPA, Sắp xếp).
    * `2`: Quản lý điểm số (Nhập, Sửa, Xóa, Xem điểm sinh viên, Xem điểm môn học).
    * `3`: Quản lý môn học (Thêm, Sửa, Xóa, Xem tất cả).
    * `10`: Lưu tất cả dữ liệu vào file Excel.
    * `0`: Thoát chương trình.
4.  Thực hiện theo các hướng dẫn trên màn hình để tương tác với từng chức năng.

## Cấu trúc file dữ liệu
Chương trình sử dụng các file Excel sau để lưu trữ dữ liệu:
* **`students.xlsx`:** Chứa thông tin chi tiết của sinh viên (MSSV, họ tên, ngày sinh, giới tính, ngành học, khóa học, khoa viện, lớp).
* **`scores.xlsx`:** Chứa thông tin điểm số của sinh viên cho từng môn học (MSSV, mã học phần, điểm chuyên cần, điểm giữa kỳ, điểm cuối kỳ, điểm tổng kết, xếp loại).
* **`subjects.xlsx`:** Chứa danh sách các môn học (mã môn học, tên môn học, số tín chỉ).

Bạn có thể xem và chỉnh sửa trực tiếp các file Excel này (đóng chương trình trước khi chỉnh sửa) để thêm hoặc sửa đổi dữ liệu. Đảm bảo cấu trúc cột trong file Excel khớp với định nghĩa của chương trình.