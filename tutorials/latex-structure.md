# Cấu trúc của file LaTeX

- **Thực hiện:** Thi Minh Nhựt - **Email:** thiminhnhut@gmail.com

- **Thời gian:** Ngày 11 tháng 08 năm 2020

---

## Cấu trúc của file LaTeX để có biên dịch ra PDF

- Cấu trúc file LaTeX:

```tex
\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{vietnam}

\begin{document}
Viết phần nội dung vào đây
\end{document}
```

- Giải thích:

  - `article`: là document class được khai báo tùy vào mục đích. Sử dụng các document class phổ biến sau: `report`, `book`, `beamer`.

  - `\usepackage[utf8]{vietnam}`: biên dịch được tiếng Việt có trong file LaTeX.

  - Nội dung của tài liệu được đặt trong cặp `\begin{document}` và `\end{document}`.

- Trong quá trình viết tài liệu, cần sử dụng package nào thì import package đó vào bằng lệnh: `\usepackage[package option]{package name}`.
