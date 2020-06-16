# Soạn thảo tài liệu khoa học với LaTeX

Thực hiện: Thi Minh Nhựt - Email: thiminhnhut@gmail.com

Thời gian bắt đầu: Ngày 31 tháng 01 năm 2017

## Giới thiệu

*Tôi không phải là người chuyên về LaTeX. Tôi sử dụng LaTeX để phục vụ cho việc
viết báo cáo các môn học trong thời gian tôi học Đại học.*

* LaTeX là chương trình soạn thảo tài liệu miễn phí, được phát triển bởi Leslie Lamport dựa trên
ngôn ngữ TeX của Donald E. Knuth. Ngày nay, LaTeX được duy trì và phát triển bởi cộng đồng người dùng TeX.

* Những điểm mạnh của LaTeX:

    + Tạo ra các bản in chuyên nghiệp và đẹp.

    + Hỗ trợ mạnh trong soạn thảo các công thức toán học và kỹ thuật.

    + Chỉ cần quan tâm nhiều đến nội dung, còn cấu trúc tài liệu, phần trình bày được tự động bởi TeX.

    + Có nhiều gói lệnh mở rộng giúp việc soạn thảo và định dạng dễ dàng hơn, đẹp hơn.

    + LaTeX là công cụ miễn phí và chạy trên nhiều hệ điều hành: Windows, Linux, Mac,...

* Những điểm yếu của LaTeX:

    + Sử dụng các lệnh để soạn thảo, gây nhiều khó khăn khi mới bắt đầu.

    + Khó khăn và mất thời gian trong việc tạo ra một kiểu trình bày mới.

    + Tạo ra các tài liệu với cấu trúc lộn xộn, nhiều định dạng,... rất mất thời gian.

    + Không nhìn thấy trước hình dáng của tài liệu trước khi biên dịch ra file PDF.

Tôi bắt đầu sử dụng LaTeX từ tháng 3 năm 2016 dùng trình soạn thảo TeXMaker với MikTeX 2.9 (trên Windows 7),
TeXLive 2013 (trên Ubuntu 14.04) và hiện nay là TeXLive 2015 (trên Ubuntu 16.04). Trong thời gian đầu tìm hiểu
LaTeX tôi gặp rất nhiều khó khăn vì mọi thứ điều mới và khó hiểu, mất nhiều thời gian để học và nó hoàn toàn
khác với soạn thảo bằng phần mềm Microsoft Word. Vì thế tôi muốn chia sẽ lại với các bạn về cách sử dụng LaTeX và
cách giải quyết các vấn đề liên quan mà tôi gặp phải trong thời gian sử dụng nhằm giúp các bạn tiết kiệm
thời gian tiếp cận và sử dụng LaTeX.

Nội dung của các bài hướng dẫn trong repository này là kết quả của quá trình tìm hiểu, tổng hợp tài liệu, thử nghiệm
và tùy chỉnh phù hợp. *Các tài liệu tham khảo đều được ghi rõ nguồn trích dẫn, đưa link về bài viết gốc.*

**Nội dung của Repository:**

* Lập trình trong TeX: [tex](https://github.com/thiminhnhut/latex/tree/master/tex)

* Cách tạo bài trình chiếu với Beamer: [beamer](https://github.com/thiminhnhut/latex/tree/master/beamer)

* Cách sử dụng một số gói lệnh hỗ trợ soạn thảo LaTeX.

* Các thủ thuật: [tips](https://github.com/thiminhnhut/latex/tree/master/tips)

## Lập trình trong TeX

1. [Cấu trúc điều khiển if](https://github.com/thiminhnhut/latex/blob/master/tex/if-condition/readme.md) 

## Tạo trình chiếu với Beamer

1. Một số thủ thuật với Beamer

    * [In tài liệu khi tạo trình chiếu với Beamer](https://github.com/thiminhnhut/latex/blob/master/beamer/beamer-tips/beamer-handout.md)

## Cách sử dụng các gói lệnh

1. [Sagetex - Gói lệnh cho phép nhúng mã Sage vào LaTeX để tính toán tự động](https://github.com/thiminhnhut/latex/tree/master/sagetex)

    * [Sử dụng Sage trong LaTeX với gói lệnh sagetex trên hệ điều hành Ubuntu](https://github.com/thiminhnhut/latex/blob/master/sagetex/make-sagetex-known-to-tex.md)

    * [Sử dụng Sage và TeXMaker để biên dịch file .tex có nhúng mã Sage với gói lệnh sagetex trên hệ điều hành Ubuntu](https://github.com/thiminhnhut/latex/blob/master/sagetex/sage-texmaker.md)

1. [References and Citations - Tạo tài liệu tham khảo và tham chiếu đến tài liệu tham khảo trong LaTeX](https://github.com/thiminhnhut/latex/tree/master/references-and-citations)

    * [biblatex - Quản lý tài liệu tham khảo trong file .bib](https://github.com/thiminhnhut/latex/tree/master/biblatex)

## Tips - Các thủ thuật

1. [Cài đặt TeXLive và TeXMaker để biên dịch tài liệu LaTeX trên hệ điều hành Ubuntu](https://github.com/thiminhnhut/ubuntu/blob/master/application/latex/caidat-texlive-texmaker.md)

1. [TeXMaker - Chương trình soạn thảo mã nguồn LaTeX](https://github.com/thiminhnhut/latex/tree/master/tips/texmaker)

    * [Cho phép sử dụng phím tắt của TeXMaker trên hệ điều hành Ubuntu 16.04](https://github.com/thiminhnhut/latex/blob/master/tips/texmaker/shortcuts-texmaker-ubuntu.md)

1. [Listings - Chèn code vào tài liệu LaTeX](https://github.com/thiminhnhut/latex/tree/master/tips/listings)

    * [Sử dụng tiếng Việt trong gói lệnh listings](https://github.com/thiminhnhut/latex/tree/master/tips/listings/tiengviet-trong-listings)

1. [Sử dụng font Time New Roman trong LaTeX với XeLaTeX hoặc LuaLaTeX](https://github.com/thiminhnhut/latex/tree/master/tips/xelatex/timenewroman)

1. [Chèn bảng trong file csv vào tài liệu LaTeX](https://github.com/thiminhnhut/latex/tree/master/tips/table-csv-latex)

1. [Đánh số tiêu đề cho các phần, các chương và các mục trong các lớp của tài liệu LaTeX](https://github.com/thiminhnhut/latex/tree/master/tips/danhso-cacmuc-tronglatex)

1. [Chuyển dấu chấm thành dấu phẩy với chế độ toán trong LaTeX](https://github.com/thiminhnhut/latex/tree/master/tips/dot2comma-math)

1. [Sử dụng font size mở rộng (24pt, 28pt) trong trình chiếu với Beamer](https://github.com/thiminhnhut/latex/tree/master/tips/font-size-extension-beamer)

1. [Xóa dấu chấm và số trang trong mục lục](https://github.com/thiminhnhut/latex/tree/master/tips/remove-dot-pagenumber-tableofcontents)

1. [Làm cho chiều rộng của bảng vừa với chiều rộng của trang trong LaTeX](https://github.com/thiminhnhut/latex/tree/master/tips/force-a-table-into-page-width)

1. [Tùy chỉnh tiêu đề của mục lục nằm ở giữa trang trong LaTeX](https://github.com/thiminhnhut/latex/tree/master/tips/tableofcontents-centering)

1. [Đánh số và tạo tham chiếu cho công thức toán trong cặp ngoặc $$](https://github.com/thiminhnhut/latex/tree/master/tips/label-ref-equal-mode-math)

1. [Định dạng text trong phần định lý của LaTeX](https://github.com/thiminhnhut/latex/tree/master/tips/theorem)

1. [LaTeX Page Styles](https://github.com/thiminhnhut/latex/tree/master/tips/pagestyle)

1. [Tạo tham chiếu cho công thức toán học, tên bảng, tên hình trong LaTeX](https://github.com/thiminhnhut/latex/tree/master/tips/label-ref)
