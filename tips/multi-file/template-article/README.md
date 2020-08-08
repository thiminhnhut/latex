# Template Article LaTeX

- **Thực hiện:** Thi Minh Nhựt - **Email:** <thiminhnhut@gmail.com>

- **Thời gian:** Ngày 08 tháng 08 năm 2020

## Nguồn tham khảo

1. [Multi-file LaTeX projects](https://www.overleaf.com/learn/latex/Multi-file_LaTeX_projects)

## Mở đầu

- Với cách quản lý thông thường, sử dụng command `\input{file}` hoặc `\include{file}` thì khi biên dịch, chúng ta cần phải quay trở về file `main.tex` để biên dịch ra tài liệu:

  - Ưu điểm: dễ thực hiện.

  - Nhược điểm: là tốn thời gian biên dịch nếu kích thước tài liệu lớn.

- Sử dụng package `standalone`, có thể biên dịch trực tiếp tài liệu từ section đó:

  - Biên dịch riêng cho section đó, không liên quan gì đến file `main.tex` do từng section có phần khai báo ban đầu khác nhau.

  - Khi nội dung của section đó hoàn thành, chúng ta quay lại file `main.tex` để import nội dung của section đó vào tài liệu.

  - Ưu điểm: linh động, thích hợp chèn các file hình vẽ được vẽ với Tikz.

  - Nhược điểm: khó sử dụng, dễ tạo ra lỗi khi biên dịch.

## Article Template

- Cần khai báo những package bắt buộc.

  ```tex
  \documentclass[12pt,a4paper]{article}
  \usepackage[subpreambles=true]{standalone}
  \usepackage[utf8]{inputenc}
  \usepackage[utf8]{vietnam}
  \usepackage{import}

  \begin{document}

  \import{sections/}{first_section}

  \end{document}
  ```

## Section Template

- Cần khai báo những package bắt buộc.

  ```tex
  \documentclass[12pt,a4paper,class=article,crop=false]{standalone}
  \usepackage[subpreambles=true]{standalone}
  \usepackage[utf8]{inputenc}
  \usepackage[utf8]{vietnam}
  \usepackage{import}

  \begin{document}

  \section{Section Template}

  \end{document}
  ```

- Chèn hình vẽ được vẽ bằng Tikz:

  ```tex
  \subimport{diagram/}{tikz-example.tex}
  ```
