# Hệ Thống Quản Lý Sinh Viên

Hệ thống quản lý sinh viên là một ứng dụng Python cho phép quản lý thông tin sinh viên, môn học, điểm số và báo cáo thống kê.

## Tính Năng Chính

### 1. Quản Lý Sinh Viên
- Thêm sinh viên mới với thông tin chi tiết
- Chỉnh sửa thông tin sinh viên
- Xóa sinh viên
- Tìm kiếm sinh viên theo MSSV
- Hiển thị danh sách sinh viên

### 2. Quản Lý Môn Học
- Thêm môn học mới
- Chỉnh sửa thông tin môn học
- Xóa môn học
- Tìm kiếm môn học theo mã môn
- Hiển thị danh sách môn học

### 3. Quản Lý Điểm Số
- Nhập điểm cho sinh viên
- Chỉnh sửa điểm
- Xóa điểm
- Tìm kiếm điểm theo MSSV
- Hiển thị bảng điểm

### 4. Báo Cáo Thống Kê
- Thống kê điểm trung bình của sinh viên
- Thống kê điểm trung bình của môn học
- Thống kê số lượng sinh viên theo khoa
- Thống kê số lượng sinh viên theo lớp

## Cấu Trúc Dự Án

```
src/
├── models/
│   ├── student.py
│   ├── subject.py
│   └── grade.py
├── managers/
│   ├── student_manager.py
│   ├── subject_manager.py
│   └── grade_manager.py
├── management/
│   ├── management.py
│   ├── menu_handler.py
│   └── student_editor.py
└── main.py
```

### Giải Thích Các Thành Phần

#### Models
- Định nghĩa cấu trúc dữ liệu cho sinh viên, môn học và điểm số
- Chứa các class và thuộc tính cơ bản

#### Managers
- Xử lý logic nghiệp vụ chính
- Quản lý thêm, sửa, xóa, tìm kiếm dữ liệu
- Tương tác với models để thực hiện các thao tác

#### Management
- `management.py`: Xử lý các chức năng chính của hệ thống
- `menu_handler.py`: Xử lý giao diện menu và điều hướng
- `student_editor.py`: Xử lý việc chỉnh sửa thông tin sinh viên

## Cài Đặt

1. Clone repository:
```bash
git clone [repository-url]
```

2. Cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

## Sử Dụng

1. Chạy chương trình:
```bash
python src/main.py
```

2. Làm theo hướng dẫn trên menu để:
   - Quản lý sinh viên
   - Quản lý môn học
   - Quản lý điểm số
   - Xem báo cáo thống kê

## Yêu Cầu Hệ Thống

- Python 3.8 trở lên
- Các thư viện Python được liệt kê trong `requirements.txt`

## Đóng Góp

Mọi đóng góp đều được hoan nghênh! Vui lòng tạo pull request hoặc issue để đóng góp.