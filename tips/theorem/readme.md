# Định dạng text trong phần định lý của LaTeX

Thực hiện: Thi Minh Nhựt - Email: thiminhnhut@gmail.com

Thời gian: Ngày 22 tháng 06 năm 2019

## Nguồn tham khảo

* [Non italic text in theorems, definitions, examples
](https://tex.stackexchange.com/questions/38260/non-italic-text-in-theorems-definitions-examples)

## Hướng dẫn cơ bản

* Sử dụng gói lệnh `\usepackage{amsmath}` với khai báo `\newtheorem{theorem}{Định lý}`:

    * Theo mặc định: phần text trong environment `theorem` sẽ được in nghiêng với định nghĩa `\theoremstyle{plain}`.

    * Muốn phần text không bị in nghiêng thì khai báo `\theoremstyle{definition}` trước khai báo `\newtheorem{theorem}{Định lý}`:

        ```tex
        \theoremstyle{definition}
        \newtheorem{theorem}{Định lý}
        ```