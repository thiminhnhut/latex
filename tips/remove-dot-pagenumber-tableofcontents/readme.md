# Xóa dấu chấm và số trang trong mục lục với tài liệu soạn bằng LaTeX

* **Thực hiện:** Thi Minh Nhựt - **Email:** thiminhnhut@gmail.com

* **Thời gian:** Ngày 06 tháng 09 năm 2017

## Nguồn tham khảo

## Nội dung

* Trong quá trình nộp đề cương chi tiết, các dấu chấm và số trang trong mục lục là không cần thiết, để xóa chúng trong LaTeX thêm các lệnh bên dưới trước `begin{document}`:

    ````latex
    \usepackage{tocloft}
    \addtocontents{toc}{\cftpagenumbersoff{chapter}}
    \addtocontents{toc}{\cftpagenumbersoff{section}}
    \addtocontents{toc}{\cftpagenumbersoff{subsection}}
    \renewcommand{\cftdot}{}
    ````
