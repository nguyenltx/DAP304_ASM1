# Project Assignment 1 môn DAP304x
## Giới thiệu
Tôi tên Lại Thanh Xuân Nguyên mã SV nguyenltxFX27584 đang học khóa PTDL tại FUNIX.\
Đây là bài làm ASM1 môn DAP304x Ứng dụng học máy trong phân tích dữ liệu.\
Dự án là một chương trình để tính toán và phân tích điểm thi của các lớp có sẵn.

## Thành phần
- File lastname_firstname_grade_the_exams.py là chương trình chính
- Folder Data Files chứa các tập tin dữ liệu là đáp án thi của từng lớp từ class1 đến class8

## Hướng dẫn sử dụng
- Chương trình sẽ yêu cầu nhập tên lớp cần phân tích điểm thi, ví dụ nhập class1 để phân tích điểm của lớp 1. Lưu ý không cần nhập đuôi file txt. Nếu nhập sai tên lớp không có trong dữ liệu chương trình sẽ báo lỗi và yêu cầu nhập lại
- Sau khi mở thành công file chương trình sẽ chạy các đoạn phân tích gồm:
    - Check nội dung file để đếm tổng số dòng trong file, số dòng không hợp lệ
    - Chấm điểm học sinh trong lớp dựa vào đáp án chuẩn và báo cáo số học sinh đạt điểm cao, điểm cao nhất, thấp nhất, trung bình...và liệt kê câu hỏi bị bỏ qua nhiều nhất cũng như trả lời sai nhiều nhất
    - Xuất ra file kết quả gồm ID của học sinh và điểm số theo từng lớp, file kết quả nằm trong folder Data Files
- Sau cùng chương trình sẽ hỏi người dùng có muốn tiếp tục kiểm tra các lớp khác không. Nếu có hãy nhập 'yes' để quay lại nhập tên file, nếu không nhập 'no' để thoát chương trình.

*Lưu ý: folder Data Files đặt đồng cấp với file py. Các file dữ liệu nằm trong Data Files*

**Cám ơn**