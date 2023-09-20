Phần mềm này được viết trên Python 3, nếu các bản mới hơn có lỗi hãy sử dụng bản này

Yêu cầu:

 - Google Chrome được cài trên máy, Bản mới nhất

 - Package:
    	+ selenium (phiên bản được sử dụng khi viết là 4.1.3)
        + reportlab (phiên bản được sử dụng khi viết là 4.0.4)
        + Pillow (phiên bản được sử dụng khi viết là 10.0.0)
Lưu ý:

 - Trong quá trình tải sẽ có thể xuất hiện các ảnh vẫn chưa load xong nhưng bị tải (những ảnh có một phần hoặc toàn bộ bị xám), khi đó dùng chế độ 2 để hoàn thiện các ảnh đó.

Cách sử dụng:
 - Cài đặt python 3(Lưu ý: add path khi cài đặt ở bước cuối cùng trước khi nhấn nút finish)
 - Tải file AJCdownload.zip
 - Giải nén file
 - Tại file AJCdownload đã giải nén, click vào đường dẫn file, nhập cmd
 - Gõ lệnh: pip install requirements.txt
    + Nếu lỗi vui lòng gõ từng lệnh [pip install Pillow==10.0.0, pip install reportlab==4.0.4, pip install selenium==4.1.3]
 - Chờ cài đặt các thư viện
 - Trong file setting.py (Chỉ sửa trong file này)
    + url : url của file cần tải(Bao gồm cả https://............)
    + trang_bat_dau: trang đầu tiên cảu file
    + trang_ket_thuc: trang kết thúc mà muốn lưu
    + output_name: tên của file (Chỉ bao gồm tên file, không có '.pdf'. VD: thaidang.pdf thì outputname = thaidang)
 - Mở lại cmd, gõ lệnh 'python openme.py' để chạy
 - Đợi khi đến chương trình thông báo 'Kết thúc'. File có thể sẽ chạy khá lâu, giữ kết nối mạng ổn định.
 - File sau khi tải sẽ ở thư mục output.