# Hệ Thống Quản Lý Sinh Viên và Điểm Số

Hệ thống quản lý thông tin sinh viên, môn học và điểm số với giao diện dòng lệnh.

## Tính Năng Chính

### Quản Lý Sinh Viên
- Thêm, sửa, xóa thông tin sinh viên
- Tìm kiếm sinh viên theo nhiều tiêu chí (MSSV, tên, lớp, khoa)
- Hiển thị danh sách sinh viên
- Sắp xếp sinh viên theo tên, GPA, MSSV
- Xem thông tin chi tiết của sinh viên

### Quản Lý Điểm Số
- Nhập điểm cho sinh viên (chuyên cần, giữa kỳ, cuối kỳ)
- Tính điểm tổng kết và xếp loại
- Xem bảng điểm của sinh viên
- Xem bảng điểm của môn học
- Thống kê điểm số (trung bình, cao nhất, thấp nhất)

### Quản Lý Môn Học
- Thêm, sửa, xóa thông tin môn học
- Quản lý số tín chỉ
- Hiển thị danh sách môn học

## Cấu Trúc Dự Án

```
src/
├── core_types/           # Các lớp cơ bản
│   ├── student.py       # Lớp Sinh viên
│   └── subject.py       # Lớp Môn học
├── managers/            # Quản lý dữ liệu
│   ├── student_manager.py
│   ├── subject_manager.py
│   └── score_manager.py
├── utils/              # Tiện ích
│   ├── file_utils.py   # Xử lý file Excel
│   ├── menu_utils.py   # Xử lý menu
│   ├── score_utils.py  # Tính toán điểm
│   └── validation_utils.py # Kiểm tra dữ liệu
├── management/         # Xử lý giao diện
│   ├── management.py   # Quản lý chính
│   └── menu_handler.py # Xử lý menu
├── main.py            # Điểm khởi chạy chương trình
└── requirements.txt   # Các thư viện cần thiết
```

## Yêu Cầu Hệ Thống

- Python 3.8 trở lên
- Thư viện: openpyxl

## Cài Đặt

1. Clone repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

## Sử Dụng

1. Chạy chương trình:
```bash
python main.py
```

2. Làm theo hướng dẫn trên menu

## Quy Tắc Dữ Liệu

### Thông Tin Sinh Viên
- MSSV: 8 chữ số
- Họ tên: Chỉ chứa chữ cái và dấu
- Ngày sinh: Định dạng dd/mm/yyyy
- Giới tính: Nam/Nữ
- Các trường khác: Không được để trống

### Thông Tin Môn Học
- Mã môn học: Không được trùng
- Tên môn học: Không được để trống
- Số tín chỉ: Số nguyên dương

### Tính Điểm
- Điểm chuyên cần: 0-10
- Điểm giữa kỳ: 0-10
- Điểm cuối kỳ: 0-10
- Điểm tổng kết = (Điểm chuyên cần * 0.4 + Điểm giữa kỳ * 0.6) * 0.5 + Điểm cuối kỳ * 0.5

### Xếp Loại
- A+: ≥ 9.5
- A: ≥ 8.5
- B+: ≥ 8.0
- B: ≥ 7.0
- C+: ≥ 6.5
- C: ≥ 5.5
- D+: ≥ 5.0
- D: ≥ 4.0
- F: < 4.0

## Lưu ý

- Dữ liệu được lưu trong các file Excel:
  - students.xlsx: Thông tin sinh viên
  - scores.xlsx: Điểm số
  - subjects.xlsx: Thông tin môn học
- Cần đảm bảo quyền truy cập file
- Nên sao lưu dữ liệu thường xuyên
- Đảm bảo các file Excel không bị mở bởi chương trình khác khi chạy

## Hạn Chế Hiện Tại

- Chưa có tính năng sao lưu/khôi phục dữ liệu
- Chưa hỗ trợ nhiều người dùng
- Chưa có báo cáo thống kê chi tiết
- Chưa có tính năng xuất báo cáo PDF

## Kế Hoạch Phát Triển

- [ ] Thêm tính năng sao lưu/khôi phục dữ liệu
- [ ] Thêm giao diện đồ họa
- [ ] Thêm báo cáo thống kê chi tiết
- [ ] Thêm tính năng xuất báo cáo PDF
- [ ] Thêm tính năng quản lý người dùng
- [ ] Chuyển sang cơ sở dữ liệu
- [ ] Thêm tính năng phân quyền
- [ ] Thêm tính năng gửi email thông báo

## Đóng Góp

Mọi đóng góp đều được hoan nghênh. Vui lòng tạo issue hoặc pull request để đóng góp.

## Giấy Phép

Dự án này được phát hành dưới giấy phép MIT.