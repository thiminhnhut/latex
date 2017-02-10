# Chuyển đổi dấu chấm thành dấu phẩy ở chế độ toán trong tài liệu LaTeX

Thực hiện: Thi Minh Nhựt - Email: thiminhnhut@gmail.com

Thời gian: Ngày 10 tháng 02 năm 2017

## Hướng dẫn cơ bản:

* File PDF: [dot2comma-math.pdf](https://github.com/thiminhnhut/latex/tree/master/tips/dot2comma-math/dot2comma-math.pdf)

* File TeX: [dot2comma-math.tex](https://github.com/thiminhnhut/latex/tree/master/tips/dot2comma-math/dot2comma-math.tex)

* Hướng dẫn cơ bản:

	+ **Cách 1:** Sử dụng lệnh `\mathcode‘\.=\mathcode‘\,`		
	
		- Đặt lệnh trên trước `\begin{document}` nếu muốn áp dụng cho toàn bộ tài liệu.
		
		- Đặt lệnh trên bên trong cặp dấu ngoặc `{ }` nếu muốn áp dụng cho một phạm vi cụ thể.
		
		- Các số được nhập vào ở chế độ toán: `$ $`, `$$ $$` hoặc các môi trường toán `align`, 
		`equation`,...
		
		- Cách thực hiện này, có khoảng trống phía sau dấu phẩy.
		
		- Ví dụ:
		
				{\mathcode‘\.=\mathcode‘\,
				
				$3.14$
				
				}
				
	+ **Cách 2:** Sử dụng lệnh `\DeclareMathSymbol{.}{\mathord}{letters}{"3B}`
	
		- Đặt trước `\begin{document}` và áp dụng cho toàn bộ tài liệu.
		
		- Các số được nhập vào ở chế độ toán: `$ $`, `$$ $$` hoặc các môi trường toán `align`, 
		`equation`,...
		
		- Cách thực hiện này, không có khoảng trống phía sau dấu phẩy.
		
	+ **Cách 3:** Sử dụng gói lệnh `siunitx`.
	
		- Khai báo:
		
				\usepackage{siunitx}
				
				\sisetup{
					
					output-decimal-marker={,}
				
				}
		
		- Các số được nhập vào ở chế độ toán: `$ $`, `$$ $$` hoặc các môi trường toán `align`, 
		`equation`,...
		
		- Ví dụ: nhập vào `$\num{3.14}$`
