# Sử dụng label và ref tạo các tham chiếu

- **Thực hiện:** Thi Minh Nhựt - **Email:** thiminhnhut@gmail.com

- **Thời gian:** Ngày 12 tháng 08 năm 2020

---

## Nội dung

- Để tham chiếu đến số thứ tự của hình, bảng, công thức toán học,... chúng ta cần phải tạo label cho nội dung đó. Cú pháp:

  ```tex
  \label{Fig:name_label} % Tạo label cho hình ảnh, tên bắt đầu bằng Fig:
  \label{Tab:name_label} % Tạo label cho bảng, tên bắt đầu bằng Tab:
  \label{Eq:name_label} % Tạo label cho công thức toán học, tên bắt đầu bằng Eq:
  \label{Chap:name_label} % Tạo label cho chapter, tên bắt đầu bằng Chap:
  \label{Sec:name_label} % Tạo label cho các loại section, tên bắt đầu bằng Sec:
  ```

- Tham chiếu đến các label đã tạo với lệnh `\ref{Name label}` với `Name label` là các tên đã tạo ở phần trên (để lấy tên của hình ảnh hoặc bảng):

  ```tex
  \ref{Fig:name_label}
  \ref{Tab:name_label}
  \ref{Eq:name_label}
  ```

- Tham chiếu đến trang của label thì dùng `\pageref{Name label}`.

- **Biên dịch:**

  - Nếu biên dịch tài liệu bằng cách thông thường thì cần phải biên dịch 2 lần mới hiển thị được tên label trong tài liệu. Nếu chỉ biên dịch một lần thì chỉ nhận được tên `??` trong tài liệu.

  - Khi sử dụng `VSCode` để biên dịch thì `VSCode` tự động làm việc này (biên dịch 2 lần) cho chúng ta.
