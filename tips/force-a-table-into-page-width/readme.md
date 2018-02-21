# Làm cho chiều rộng của bảng vừa với chiều rộng của trang trong LaTeX

Sưu tầm: Thi Minh Nhựt - Email: thiminhnhut@gmail.com

Thời gian: Ngày 21 tháng 02 năm 2018

## Tài liệu tham khảo

Chủ đề: [How to force a table into page width?](https://tex.stackexchange.com/questions/10535/how-to-force-a-table-into-page-width)

## Hướng dẫn thực hiện

* Sử dụng package [tabularx](http://www.ctan.org/pkg/tabularx).

* Cú pháp:

        \usepackage{tabularx} % in the preamble
        %....
        \begin{tabularx}{\textwidth}{|X|X|}
        \hline
        \textbf{Symptom} & \textbf{Metric} \\
        \hline
        \end{tabularx}
