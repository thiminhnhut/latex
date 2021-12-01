# Sử dụng font Times New Roman trong LaTeX với XeLaTeX hoặc LuaLaTeX

Thực hiện: Thi Minh Nhựt - Email: thiminhnhut@gmail.com

Thời gian: Ngày 03 tháng 02 năm 2017

## Hướng dẫn cơ bản:

- File PDF: [sudungfont_timesnewroman.pdf](https://github.com/thiminhnhut/latex/tree/master/tips/xelatex/timenewroman/sudungfont_timesnewroman.pdf)

- File TeX: [sudungfont_timesnewroman.tex](https://github.com/thiminhnhut/latex/tree/master/tips/xelatex/timenewroman/sudungfont_timesnewroman.tex)

- Hướng dẫn:

  - Biên dịch với XeLaTeX hoặc LuaLaTeX:

    - Cần khai báo:

      ```latex
      \usepackage{fontspec}
      \setmainfont{Times New Roman}
      ```

    - Soạn thảo tài liệu như bình thường.

    - Các tên mặc định hiển thị dạng tiếng Anh, cần định nghĩa thành tiếng Việt (xem hướng dẫn trong file PDF).

    - Chọn biên dịch bằng XeLaTeX trên TeXMaker.

  - Biên dịch bằng PDFLaTeX:

    - Cần khai báo:

      ```latex
      \usepackage[utf8]{inputenc}
      \usepackage[utf8]{vietnam}
      \usepackage{times}
      ```

    - Các tên mặc định được hiển thị bằng Tiếng Việt.

    - Chọn biên dịch bằng PDFLaTeX trên TeXMaker.
