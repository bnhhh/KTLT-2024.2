# Hệ Thống Quản Lý Sinh Viên

## Mô tả
Đây là hệ thống quản lý sinh viên sử dụng Python, lưu trữ dữ liệu bằng file Excel. Hệ thống hỗ trợ quản lý sinh viên, môn học, điểm số, tính GPA, xếp loại, và các chức năng tìm kiếm, sắp xếp, thống kê.

## Tính năng chính

- **Quản lý sinh viên:** Thêm, sửa, xóa, tìm kiếm, sắp xếp, hiển thị danh sách sinh viên.
- **Quản lý môn học:** Thêm, sửa, xóa, tìm kiếm, hiển thị danh sách môn học.
- **Quản lý điểm số:** Nhập, sửa, xóa điểm; xem điểm sinh viên, xem điểm theo môn; tự động tính GPA và xếp loại.
- **Tìm kiếm, sắp xếp:** Tìm kiếm sinh viên theo MSSV, tên, lớp, khoa; sắp xếp theo tên, GPA, MSSV.
- **Kiểm tra hợp lệ dữ liệu:** Kiểm tra đầu vào cho MSSV, mã môn, tín chỉ, điểm số, v.v.
- **Tự động xóa điểm khi xóa môn học.**

## Yêu cầu hệ thống

- Python 3.8 trở lên
- Thư viện: `openpyxl`

## Cài đặt

1. **Clone repository:**
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```
2. **Cài đặt các thư viện cần thiết:**
   ```bash
   pip install -r requirements.txt
   ```

## Hướng dẫn sử dụng

1. Chạy file `main.py` để bắt đầu chương trình:
   ```bash
   python main.py
   ```
2. Làm theo hướng dẫn trên menu để quản lý sinh viên, môn học, điểm số.

## Cấu trúc các file chính và chức năng

- **main.py**: Điểm khởi động chương trình, hiển thị menu chính.
- **management/management.py**: Lớp trung tâm quản lý toàn bộ hệ thống, điều phối các thao tác giữa sinh viên, môn học, điểm số.
- **management/menu_handler.py**: Xử lý giao diện dòng lệnh, nhập/xuất dữ liệu từ người dùng, gọi các chức năng thêm/sửa/xóa/tìm kiếm/sắp xếp.
- **managers/student_manager.py**: Thêm, sửa, xóa, tìm kiếm, sắp xếp sinh viên, hiển thị danh sách sinh viên.
- **managers/subject_manager.py**: Thêm, sửa, xóa, tìm kiếm môn học, hiển thị danh sách môn học.
- **managers/score_manager.py**: Thêm, sửa, xóa điểm, xem điểm sinh viên, xem điểm theo môn, xóa điểm khi xóa môn học.
- **core_types/student.py**: Định nghĩa đối tượng Sinh viên, các phương thức tính GPA, chuyển đổi dữ liệu.
- **core_types/subject.py**: Định nghĩa đối tượng Môn học, chuyển đổi dữ liệu.
- **utils/validation_utils.py**: Kiểm tra hợp lệ MSSV, mã môn, tín chỉ, tên, ngày sinh, ...
- **utils/score_utils.py**: Tính điểm tổng kết, GPA, xếp loại, kiểm tra hợp lệ điểm số.
- **utils/file_utils.py**: Đọc và ghi dữ liệu từ/đến file Excel.
- **utils/menu_utils.py**: Hỗ trợ hiển thị menu, xử lý lựa chọn menu.

## Cấu trúc chương trình

```
src/
├── core_types/           # Các lớp đối tượng cơ bản (Sinh viên, Môn học)
│   ├── student.py
│   └── subject.py
├── managers/             # Quản lý dữ liệu sinh viên, môn học, điểm số
│   ├── student_manager.py
│   ├── subject_manager.py
│   └── score_manager.py
├── utils/                # Các hàm tiện ích, kiểm tra, tính toán, xử lý file, menu
│   ├── file_utils.py
│   ├── menu_utils.py
│   ├── score_utils.py
│   └── validation_utils.py
├── management/           # Xử lý giao diện, menu, điều phối hệ thống
│   ├── management.py
│   └── menu_handler.py
├── main.py               # Điểm khởi động chương trình
└── requirements.txt      # Thư viện cần thiết
```

## Quy tắc dữ liệu

- **Sinh viên:**
  - MSSV: 8 chữ số, duy nhất.
  - Họ tên: Chỉ chứa chữ cái và dấu.
  - Ngày sinh: Định dạng dd/mm/yyyy.
  - Giới tính: Nam/Nữ.
  - Các trường khác: Không được để trống.

- **Môn học:**
  - Mã môn học: Không được trùng.
  - Tên môn học: Không được để trống.
  - Số tín chỉ: Số nguyên dương.

- **Điểm số:**
  - Điểm chuyên cần, giữa kỳ, cuối kỳ: 0-10.
  - Điểm tổng kết = (Điểm chuyên cần * 0.4 + Điểm giữa kỳ * 0.6) * 0.5 + Điểm cuối kỳ * 0.5

- **Xếp loại theo GPA:**
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
  - `students.xlsx`: Thông tin sinh viên
  - `subjects.xlsx`: Thông tin môn học
  - `scores.xlsx`: Điểm số
- Khi xóa môn học sẽ tự động xóa toàn bộ điểm của môn đó.
- Đảm bảo các file Excel không bị mở bởi chương trình khác khi chạy.
- Nên sao lưu dữ liệu thường xuyên.

## Hạn chế hiện tại

- Chưa có tính năng sao lưu/khôi phục dữ liệu tự động.
- Chưa hỗ trợ nhiều người dùng hoặc phân quyền truy cập.
- Chưa có giao diện đồ họa (GUI), chỉ sử dụng dòng lệnh.
- Chưa có báo cáo thống kê chi tiết hoặc xuất báo cáo PDF.
- Chưa tích hợp gửi email thông báo.
- Chưa chuyển sang sử dụng cơ sở dữ liệu thực thụ (chỉ dùng file Excel).

## Kế hoạch phát triển

- [ ] Thêm tính năng sao lưu/khôi phục dữ liệu tự động.
- [ ] Thêm giao diện đồ họa (GUI).
- [ ] Thêm báo cáo thống kê chi tiết, xuất báo cáo PDF.
- [ ] Thêm tính năng gửi email thông báo.
- [ ] Hỗ trợ nhiều người dùng, phân quyền truy cập.
- [ ] Chuyển sang sử dụng cơ sở dữ liệu (MySQL, SQLite, ...).
- [ ] Tối ưu hiệu năng và bảo mật dữ liệu.

