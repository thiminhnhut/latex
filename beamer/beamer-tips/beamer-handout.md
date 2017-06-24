# In tài liệu trong trình chiếu với Beamer

Tìm hiểu: Thi Minh Nhựt - Email: thiminhnhut@gmail.com

Thời gian: Ngày 24 tháng 06 năm 2017

## Nội dung

1. Khi tạo trình chiếu với Beamer nếu có sử dụng các overlay để tạo 
hiệu ứng chuyển slide, khi in ấn thì có thể chúng ta không cần đến những
hiệu ứng này.

	+ Mục đích bỏ đi những overlay: có cái nhìn tổng quát về nội dung của
	bài báo cáo.
	
	+ Cách thực hiện: thêm tùy chọn `handout`.
	
	```latex
	
	\documentclass[handout]{beamer}
	
	```
	
1. In nhiều frame trên một mặt giấy: Khi gửi bài báo cáo cho người nghe
có thể chúng ta cần in nhiều frame trên một mặt giấy.

	+ Mục đích: tiết kiệm giấy và việc in một frame trên một trang giấy
	là không cần thiết.
	
	+ Cách thực hiện: sử dụng gói lệnh `pgfpages`.
	
	```latex
	\usepackage{pgfpages}
	
	\pgfpagesuselayout{4 on 1}[a4paper,border shrink=5mm,landscape]
	
	```
	
	+ Ví dụ như lệnh bên trên: in 4 frame trên một mặt giấy a4 với khổi
	giấy nằm ngang với khoảng cách giữa các frame theo chiều dọc là 5mm.
