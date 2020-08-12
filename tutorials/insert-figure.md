# Chèn hình ảnh

- **Thực hiện:** Thi Minh Nhựt - **Email:** thiminhnhut@gmail.com

- **Thời gian:** Ngày 12 tháng 08 năm 2020

---

## Nội dung

- Sử dụng package `graphicx` để cho phép chèn hình ảnh vào tài liệu. Trỏ đến thư mục chứa hình ảnh cần chèn với lệnh `\graphicspath{list_dir}` (path format theo linux).

  ```tex
  \usepackage{graphicx}
  \graphicspath{{folder/}{folder2/}}
  ```

  chú ý folder format theo `{folder2/}` (có dấu `/` cuối).

- Sử dụng môi trường `figure` để tạo `caption` và `label` cho hình ảnh. Chèn hình bằng lệnh `\includegraphics[option]{imange_name}`.

  - Cú pháp:

    ```tex
    \begin{figure}
      \centering
      \includegraphics[scale=1.0]{vscode-latex}
      \caption{Name figure}
      \label{Fig:name_label}
    \end{figure}
    ```

  - Giải thích:

    - `\centering`: căn hình ảnh nằm giữa.

    - `\includegraphics[scale=1.0]{vscode-latex}`: chèn hình ảnh với option `scale=1.0` (giữ nguyên). Ngoài ra còn một số option khác: `angle=90` (quy ước chiều theo đường tròn lượng giác).

    - `\caption{Name figure}`: ghi tên cho hình ảnh. Cấu trúc đầy đủ của lệnh `caption` là: `\caption[Tên hiển thị của hình trong danh sách hình]{Tên hiển thị của hình trong tài liệu}`. Nếu không muốn đặt tên cho figure thì bỏ lệnh `\caption`.

    - `\label{Fig:name_label}`: tạo label tham chiếu cho hình ảnh. Với hình ảnh thì tên label nên bắt đầu bằng `Fig:name_label` để thuận tiện cho quá trình tìm label sau này.

  - Số thứ tự của hình ảnh sẽ được đánh số tự động theo cấu trúc của tài liệu.

  - Hình thức format của caption có thể tùy chỉnh theo ý của tác giả (phần này được trình bày ở phần khác). (TODO)
