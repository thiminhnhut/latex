# Đánh số cho tiêu đề các phần, các chương và các mục trong tài liệu LaTeX

Thực hiện: Thi Minh Nhựt - Email: thiminhnhut@gmail.com

Thời gian: Ngày 06 tháng 02 năm 2017

## Hướng dẫn cơ bản:

* File PDF: [danhso-cacmuc-tronglatex.pdf](https://github.com/thiminhnhut/latex/tree/master/tips/danhso-cacmuc-tronglatex/danhso-cacmuc-tronglatex.pdf)

* File TeX: [danhso-cacmuc-tronglatex.tex](https://github.com/thiminhnhut/latex/tree/master/tips/danhso-cacmuc-tronglatex/danhso-cacmuc-tronglatex.tex)

* Các file TeX ví dụ: [examples](https://github.com/thiminhnhut/latex/tree/master/tips/danhso-cacmuc-tronglatex/examples)

* Hướng dẫn cơ bản:

	+ Dùng các lệnh `\part`, `\chapter`, `\section`, `\subsection`, `\subsubsection` 
	và `\paragraph`, `\subparagraph` để đánh số cho các tiêu đề của các lớp `article`, 
	`report` và `book` trong tài liệu LaTeX.
	
	+ Trong mỗi lớp sẽ có một số cấp độ không tự đánh số do mặc định. 
	Chúng ta có thể đánh số cho tất cả các cấp độ trên (7 cấp độ).	
	
	|Cấp độ | Lệnh           | Có trong các lớp                                 |
	|:-----:|:---------------|:-------------------------------------------------| 
	|-1     | \part          | book 			                                |
	|0      | \chapter       | report và book                                   |
	|1      | \section       | article, report và book                          |
	|2      | \subsection    | article, report và book                          |
	|3      | \subsubsection | Không đánh số trong lớp report và book           |
	|4      | \paragraph     | Không đánh số trong lớp article, report và book  |
	|5      | \subparagraph  | Không đánh số trong lớp article, report và book  |
	
	+ Đánh số cho các cấp độ và thêm nội dung của chúng vào mục lục, các cấp độ được cho trên bảng trên.
	
			\setcounter{secnumdepth}{cấp_độ}
			
			\setcounter{secnumdepth}{cấp_độ}
			
	+ Xem hướng dẫn trong mục 2 trong file [danhso-cacmuc-tronglatex.pdf](https://github.com/thiminhnhut/latex/tree/master/tips/danhso-cacmuc-tronglatex/danhso-cacmuc-tronglatex.pdf)
	
	+ Các file tex ví dụ: [examples/cachdanhso](https://github.com/thiminhnhut/latex/tree/master/tips/danhso-cacmuc-tronglatex/examples/cachdanhso)
	
	+ Ví dụ:
		
		- Đánh số cho đến các lệnh `\paragraph` hoặc `\subparagraph`:
	
				\setcounter{secnumdepth}{4} hoặc \setcounter{secnumdepth}{5}
			
		- Thêm nội dung của các lệnh cho đến các lệnh `\paragraph` hoặc `\subparagraph` vào mục lục:
	
				\setcounter{tocdepth}{4} hoặc \setcounter{tocdepth}{5}
			
		- Làm cho các lệnh `\paragraph` và `\subparagraph` giống như các cấp độ trước nó 
		(tự động xuống dòng và canh thẳng hàng), ta định nghĩa lại chúng như sau:
	
				\newcommand{\parasection}[1]{\paragraph{#1}\mbox{}\medskip\par}
			
				\newcommand{\subparasection}[1]{{\setlength{\parindent}{0pt}\subparagraph{#1}\mbox{}\medskip\par}}
	
		- Dùng lệnh `\parasection` thay cho lệnh `\paragraph`.
	
		- Dùng lệnh `\subparasection` thay cho lệnh `\subparagraph`
		
	+ Cách thay đổi các nhãn mặc định của các tiêu đề trong các lớp tài liệu: 
	
		- Xem hướng dẫn ở mục 3 trong file [danhso-cacmuc-tronglatex.pdf](https://github.com/thiminhnhut/latex/tree/master/tips/danhso-cacmuc-tronglatex/danhso-cacmuc-tronglatex.pdf)
		
		- Các file tex ví dụ: [examples/thaydoi-cachdanhso](https://github.com/thiminhnhut/latex/tree/master/tips/danhso-cacmuc-tronglatex/examples/thaydoi-cachdanhso)
