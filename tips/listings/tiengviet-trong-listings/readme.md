# Sử dụng tiếng Việt trong gói lệnh listings

Thực hiện: Thi Minh Nhựt - Email: thiminhnhut@gmail.com

Thời gian: Ngày 02 tháng 02 năm 2017

## Hướng dẫn cơ bản:

* File TeX cài tiếng Việt trong gói lệnh listings: [tvietlistings.sty](https://github.com/thiminhnhut/latex/tree/master/tips/listings/tiengviet-trong-listings/tvietlistings.sty)

* File hướng dẫn PDF: [tiengviet-trong-listings.pdf](https://github.com/thiminhnhut/latex/tree/master/tips/listings/tiengviet-trong-listings/tiengviet-trong-listings.pdf)

* File TeX của bài hướng dẫn: [tiengviet-trong-listings.tex](https://github.com/thiminhnhut/latex/tree/master/tips/listings/tiengviet-trong-listings/tiengviet-trong-listings.tex)

* Các file TeX ví dụ: [examples](https://github.com/thiminhnhut/latex/tree/master/tips/listings/tiengviet-trong-listings/examples)

* Hướng dẫn:

	+ Khai báo trước `\begin{document}`:
	
			\usepackage[vietnamese.licr]{babel}
			
			\usepackage{listings}
			
			\usepackage{tvietlistings}
			
	+ Địa chỉ tải về các gói lệnh trên (nếu chưa cài đặt):
	
		- `babel-vietnamese`: [Download](https://www.ctan.org/pkg/babel-vietnamese)
		
		- `listings`: [Download](https://www.ctan.org/pkg/listings)
		
		- `tvietlistings`: [Download](https://github.com/thiminhnhut/latex/tree/master/tips/listings/tiengviet-trong-listings/tvietlistings.sty). 
		File `tvietlistings.sty` tải về đặt trong thư mục chung với file `.tex` đang soạn thảo.
		
	+ Sử dụng các lệnh trong gói lệnh `listings` như bình thường, nhưng hạn chế sử dụng tùy chọn 
	`columns=flexible` hoặc `columns=fullflexible` vì các chữ tiếng Việt có thể bị dính nhau.
