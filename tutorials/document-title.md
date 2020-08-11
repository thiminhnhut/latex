# Document Title

- **Thực hiện:** Thi Minh Nhựt - **Email:** thiminhnhut@gmail.com

- **Thời gian:** Ngày 11 tháng 08 năm 2020

---

## Sử dụng title mặc định

- Cấu trúc:

  ```tex
  \documentclass{article}

  \title{Title}
  \author{Author}
  \date{Date}

  \begin{document}
  \maketitle
  \end{document}
  ```

- Giải thích:

  - `\title{Nội dung của title}`.

  - `\author{Thông tin của tác giả}`.

  - `\date{Thời gian}`. Nếu muốn sử dụng thời gian hiện tại thì dùng `\date{\today}`.

  - `\maketitle`: xuất thông tin của title ra file pdf. Nếu không sử dụng lệnh này thì thông tin của title không được xuất ra file pdf.

## Sử dụng title mà tác giả tự định nghĩa

- Sử dụng môi trường `title`.

  ```tex
  \documentclass{article}

  \begin{document}

    \begin{titlepage}
      Nội dung của title tự định nghĩa
    \end{titlepage}

  \end{document}
  ```
