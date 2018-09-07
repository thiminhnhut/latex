# Tùy chỉnh tiêu đề của mục lục nằm ở giữa trang

Thực hiện: Thi Minh Nhựt - Email: thiminhnhut@gmail.com

Thời gian: Ngày 07 tháng 09 năm 2018

## Nguồn tham khảo

* [formatting of the table of contents](https://tex.stackexchange.com/questions/157396/formatting-of-the-table-of-contents)

## Nội dung thực hiện

* Sử dụng package: ``tocstyle``, với khai báo sau:

    ```
    \usepackage[tocflat]{tocstyle}
    \usetocstyle{standard}

    % Redefinition of ToC command to get centered heading
    \makeatletter
    \renewcommand\tableofcontents{%
      \null\hfill\textbf{\Large\contentsname}\hfill\null\par
      \@mkboth{\MakeUppercase\contentsname}{\MakeUppercase\contentsname}%
      \@starttoc{toc}%
    }
    \makeatother
    ```

* Ví dụ: [example](https://github.com/thiminhnhut/latex/tree/master/tips/tableofcontents-centering/examples)
