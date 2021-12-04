# Quản lý tài liệu viết bằng LaTeX có nội dung lớn

- **Thực hiện:** Thi Minh Nhựt - **Email:** thiminhnhut@gmail.com

- **Thời gian:** Ngày 27 tháng 11 năm 2021

---

## Đặt vấn đề

- Khi soạn thảo các tài liệu có nội dung lớn trong LaTeX ví dụ:
  `report class`, `book class`, mỗi lần có sự thay đổi về nội dụng
  (viết thêm, sửa đổi nội dung của tài liệu) thì chúng ta thực hiện
  build lại toàn bộ tài liệu (bao gồm những phần không thay đổi và
  những phần thay đổi), việc này rất tốn thời gian và tài nguyên máy
  vì chúng ta chỉ cần xem những nội dung đã thay đổi nhưng lại thực
  hiện build lại toàn bộ tài liệu.

- Để khắc phục tình trạng trên, chúng ta thực hiện chia nhỏ tài liệu
  ra, thay đổi nội dung của phần nào chỉ thực hiện build lại nội dung
  của phần đó. Khi viết thêm, sửa đổi nội dung của từng phần thành công
  thì tiến hành kết hợp các phần đó lại thành một tài liệu hoàn thiện
  và tiến hành build lại toàn bộ tài liệu.

- Có một lý do khác là việc chia nhỏ tài liệu ra thành những phần nhỏ giúp cho
  việc quản lý tài liệu dễ dàng hơn (khi cần chỉnh sửa phần nào thì chúng ta đi
  đến đúng file chứa nội dung của phần đó và thực hiện sửa đổi).

## Ví dụ để viết tài liệu luận văn

- Để viết luận văn, chúng ta thường sử dụng `report class`.

- Ví dụ, nội dung của luận văn gồm có 4 chương như sau:

  - Trang bìa.

  - Chương 1 - Tổng quan về đề tài nghiên cứu.

    - Giới thiệu đề tài.

    - Phạm vi nghiên cứu.

    - Phương pháp nghiên cứu.

  - Chương 2 - Cơ sở lý thuyết.

    - Lý thuyết về nội dung số 1.

    - Lý thuyết về nội dung số 2.

    - Lý thuyết về nội dung số 3.

## Cách thực hiện

Chúng ta có một số cách thực hiện như sau:

1. Sử dụng command `include` và `includeonly`:

   - Cấu trúc của folder:

     ```bash
     |--chapter
              |-- chapter01
                  |--chapter01.tex
                  |--section01.tex
                  |--section02.tex
              |--chapter02
                  |--chapter02.tex
                  |--section02.tex
                  |--section02.tex
              ...
     |--cover
              |--cover.tex
     |--main.tex
     ```

   - Viết nội dung của từng chapter/section trong những file riêng biệt (ví dụ
     theo cấu trúc bên trên).

   - File `main.tex` có nội dung như sau:

     ```latex
      \includeonly{
        % cover/cover,
        % chapter/chapter01/chapter01,
        % chapter/chapter02/chapter02,
      }

      \begin{document}
      \include{cover/cover}

      \tableofcontents

      \include{chapter/chapter01/chapter01}

      \include{chapter/chapter02/chapter02}

      \end{document}
     ```

     - Nếu muốn build nội dung của chapter nào thì uncomment dòng chứa tên của chappter
       đó trong lệnh `\includeonly`.

     - Nếu muốn build toàn bộ tài liệu thì uncomment luôn cả lệnh `\includeonly`:

       ```latex
       %\includeonly{
        % cover/cover,
        % chapter/chapter01/chapter01,
        % chapter/chapter02/chapter02,
       %}
       ```

   - Project mẫu minh họa cho hướng dẫn trên: [include-includeonly](https://github.com/thiminhnhut/latex/blob/master/tutorials/large-document/include-includeonly)
