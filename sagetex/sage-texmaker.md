# Sử dụng Sage và TeXMaker để biên dịch file .tex có nhúng mã Sage với gói lệnh sagetex trên hệ điều hành Ubuntu

Thực hiện: Thi Minh Nhựt - Email: thiminhnhut@gmail.com

Thời gian: Ngày 31 tháng 01 năm 2017

## Nguồn tham khảo

[How do I write a custom command to enable Sage in Texmaker?](https://goo.gl/GmLEWx) trên [TeX - LaTeX Stack Exchange](http://tex.stackexchange.com/)

## Cách thực hiện

* **Bước 1:** Mở TeXMaker, trên thanh menu chọn `User/User Commands/Edit User Commands`, 
được giao diện như hình bên dưới:

	![](https://raw.githubusercontent.com/thiminhnhut/latex/master/sagetex/images/sage-texmaker-1.png)

* **Bước 2:** Điền các lệnh sau để sử dụng trực tiếp TeXMaker biên dịch tài liệu có nhúng mã `Sage`.

	+ Ví dụ, chọn `Command 1:` (các bạn có thể chọn các `Command` khác).
	
	+ Trong ô `Menu Item` bạn điền vào: `Sage` (các bạn có thể đặt tên khác).
	
	+ Trong ô `Command (%: filename without extension)` bạn điền: `sage %.sagetex.sage`.
	
	+ Tóm lại, kết quả điền vào được mô tả như hình bên dưới:
	
	![](https://raw.githubusercontent.com/thiminhnhut/latex/master/sagetex/images/sage-texmaker-2.png)

## Cách biên dịch tài liệu LaTeX có nhúng mã Sage

* Chúng ta biên dịch theo trình tự sau: `PDFLaTeX - Sage - PDFLaTeX - View PDF`.

	+ Biên dịch với `PDFLaTeX` lần 1:
	
	![](https://raw.githubusercontent.com/thiminhnhut/latex/master/sagetex/images/compile-pdflatex.png)
	
	+ Biên dịch với `Sage`:
	
	![](https://raw.githubusercontent.com/thiminhnhut/latex/master/sagetex/images/compile-sage.png)
	
	+ Biên dịch với `PDFLaTeX` lần 2:
	
	![](https://raw.githubusercontent.com/thiminhnhut/latex/master/sagetex/images/compile-pdflatex.png)

	+ Cuối cùng chọn `View PDF` để xem kết quả.
	
* Nếu các mã `Sage` của chúng ta có lỗi (do lỗi cú pháp) thì bước biên dịch với `Sage` sẽ không thành công.

	+ Cách giải quyết: cần biên dịch file `ten_file.sagetex.sage` ở chế độ command line 
	và tìm ra lỗi sai để sửa lỗi và biên dịch lại. 
	
	+ Chuyển đến thư mục chứa file `ten_file.sagetex.sage` của file `ten_file.tex` đang soạn. 
	Chọn menu `Tools/Open Terminal` để mở cửa sổ Terminal ở thư mục làm việc. Rồi thực hiện lệnh bên dưới.
	
			$ sage ten_file.sagetex.sage
	
		Bước này sẽ gợi ý về thông báo lỗi cú pháp. Dựa theo gợi ý này tìm và sửa lỗi trong file `ten_file.tex`.
	
	+ Sau đó biên dịch lại từ đầu: `PDFLaTeX - Sage`, biên dịch và sửa lỗi cho đến khi không còn thông báo lỗi.
	
	+ Khi không còn thông báo lỗi biên dịch theo trình tự sau: `PDFLaTeX - Sage - PDFLaTeX - View PDF` 
	để xem kết quả tính toán tự động trong file PDF.

* Xem thêm cách cài đặt `SageMath` trên hệ điều hành Ubuntu và làm cho `Sagetex` biết `TeX` để biên dịch được 
tài liệu có nhúng mã `Sage`: [Cách thực hiện](https://github.com/thiminhnhut/latex/tree/master/sagetex/make-sagetex-known-to-tex.md)
