# Chèn bảng

- **Thực hiện:** Thi Minh Nhựt - **Email:** thiminhnhut@gmail.com

- **Thời gian:** Ngày 12 tháng 08 năm 2020

---

## Nội dung

- Sử dụng môi trường `table` để tạo `caption` và `label` cho bảng.

  - Cú pháp:

    ```tex
    \begin{table}
      \centering
      \caption{Name figure}
      \label{Fig:name_label}
      \begin{tabular}{|c|c|c|} \hline
        Cột 1 & Cột 2 & Cột 3 \\ \hline
      \end{tabular}
    \end{table}
    ```

  - Giải thích:

    - `\centering`: căn bảng nằm giữa.

    - Tạo bảng bằng môi trường `tabular`. Sử dụng dấu `|` để kẻ vạch đứng cho bảng, `\hline` để kẻ vạch ngang cho bảng. Căn nội dung của từng cột trong bảng với `c (center), l (left), r (right)`. Sử dụng `&` để phân cách nội dung giữa các cột trong bảng. Kết thúc mỗi hàng là dấu `\\` (xuống dòng).

    - `\caption{Name table}`: ghi tên cho bảng. Cấu trúc đầy đủ của lệnh `caption` là: `\caption[Tên hiển thị của bảng trong danh sách bảng]{Tên hiển thị của bảng trong tài liệu}`. Nếu không muốn đặt tên cho table thì bỏ lệnh `\caption`.

    - `\label{Tab:name_label}`: tạo label tham chiếu cho bảng. Với bảng thì tên label nên bắt đầu bằng `Tab:name_label` để thuận tiện cho quá trình tìm label sau này.

  - Số thứ tự của bảng sẽ được đánh số tự động theo cấu trúc của tài liệu.

  - Hình thức format của caption có thể tùy chỉnh theo ý của tác giả (phần này được trình bày ở phần khác). (TODO)
