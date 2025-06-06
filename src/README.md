# Hệ Thống Quản Lý Sinh Viên và Điểm Số

Hệ thống quản lý sinh viên và điểm số là một ứng dụng Python được thiết kế để quản lý thông tin sinh viên, môn học và điểm số trong môi trường giáo dục.

## Tính năng chính

### 1. Quản lý Sinh viên
- Thêm, sửa, xóa thông tin sinh viên
- Tìm kiếm sinh viên theo nhiều tiêu chí
- Hiển thị danh sách sinh viên
- Tính điểm trung bình (GPA) và xếp loại
- Sắp xếp danh sách sinh viên

### 2. Quản lý Môn học
- Thêm, sửa, xóa thông tin môn học
- Quản lý số tín chỉ
- Hiển thị danh sách môn học

### 3. Quản lý Điểm số
- Nhập điểm cho sinh viên
- Tính điểm tổng kết
- Xếp loại học lực
- Xem điểm theo sinh viên hoặc môn học

## Yêu cầu hệ thống

- Python 3.x
- Thư viện openpyxl
- Hệ điều hành: Windows/Linux/MacOS

## Cài đặt

1. Clone repository:
```bash
git clone [repository-url]
```

2. Cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

## Cấu trúc thư mục

```
project/
│
├── src/
│   ├── core_types/
│   │   ├── student.py
│   │   └── subject.py
│   │
│   ├── managers/
│   │   ├── student_manager.py
│   │   ├── subject_manager.py
│   │   └── score_manager.py
│   │
│   └── management/
│       ├── management.py
│       └── menu_handler.py
│
├── data/
│   ├── students.xlsx
│   ├── subjects.xlsx
│   └── scores.xlsx
│
├── README.md
└── requirements.txt
```

## Hướng dẫn sử dụng

1. Chạy chương trình:
```bash
python main.py
```

2. Menu chính:
   - Quản lý sinh viên
   - Quản lý điểm số
   - Quản lý môn học
   - Lưu dữ liệu
   - Thoát chương trình

3. Quản lý sinh viên:
   - Thêm sinh viên mới
   - Sửa thông tin sinh viên
   - Xóa sinh viên
   - Tìm kiếm sinh viên
   - Hiển thị tất cả sinh viên
   - Xem điểm trung bình và xếp loại
   - Sắp xếp danh sách sinh viên

4. Quản lý điểm số:
   - Nhập điểm cho sinh viên
   - Sửa điểm sinh viên
   - Xóa điểm
   - Xem điểm sinh viên

5. Quản lý môn học:
   - Thêm môn học mới
   - Sửa thông tin môn học
   - Xóa môn học
   - Xem tất cả môn học

## Quy tắc nhập liệu

### Sinh viên
- Mã số sinh viên: 8 chữ số
- Họ tên: Chỉ chứa chữ cái và dấu cách
- Ngày sinh: Định dạng dd/mm/yyyy
- Giới tính: Nam hoặc Nữ

### Môn học
- Mã môn học: Không được trùng lặp
- Tên môn học: Không được để trống
- Số tín chỉ: Số nguyên dương

### Điểm số
- Điểm chuyên cần: 0-10
- Điểm giữa kỳ: 0-10
- Điểm cuối kỳ: 0-10

## Lưu ý

- Dữ liệu được lưu tự động vào file Excel
- Nên sao lưu dữ liệu thường xuyên
- Kiểm tra kỹ thông tin trước khi nhập

## Đóng góp

Mọi đóng góp đều được hoan nghênh. Vui lòng tạo issue hoặc pull request để đóng góp.
