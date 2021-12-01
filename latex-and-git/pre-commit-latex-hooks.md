# Sử dụng Git và LaTeX - pre-commit-latex-hooks

- **Thực hiện:** Thi Minh Nhựt - **Email:** thiminhnhut@gmail.com

- **Thời gian:** Ngày 30 tháng 10 năm 2021

---

## Nội dung

- Để có thể hiểu được nội dung của phần này, bạn cần có một số kiến thức cơ bản
  về việc sử dụng `git`.

- [Git](https://git-scm.com/) là một công cụ vô cùng mạnh mẻ trong việc quản lý
  mã nguồn, đặc biệt khi chúng ta làm việc với các thành viên trong nhóm.

- Với một project `LaTeX` mà có nhiều thành viên cùng tham gia, chúng ta sẽ gặp
  vấn đề như sau:

  - Mỗi người có một style viết code `LaTeX` riêng, làm mất sự thống nhất
    . Mặc dù hình thức chúng ta viết trong file `.tex` không ảnh hưởng kết quả
    xuất ra file `.pdf` nhưng sau này muốn tiếp tục duy trì project sẽ gặp khó khăn,
    nên tốt nhất là chúng ta nên tạo ra một format chung cho tất cả các thành viên.

  - Để giải quyết vấn đề trên, chúng ta sử dụng module `pre-commit` và
    `pre-commit-latex-hooks` để kiểm tra format của các file `.tex` trước khi
    `commit`: module `pre-commit` sẽ giúp chúng ta sửa và gợi ý cách sửa cho đến
    khi format code latex phù hợp với các quy ước đặt ra.

- Cách thực hiện:

  1. Cài đặt [python](https://www.python.org/downloads/).

  1. Cài đặt [Rust](https://www.rust-lang.org/tools/install)

  1. Cài đặt module `pre-commit`:

     ```bash
     pip install pre-commit
     ```

  1. Tạo file `.pre-commit-config.yaml` với nội dung như sau:

     ```yaml
     repos:
       - repo: https://github.com/pre-commit/pre-commit-hooks
         rev: v4.0.1
         hooks:
           - id: trailing-whitespace
           - id: end-of-file-fixer
       - repo: https://github.com/jonasbb/pre-commit-latex-hooks
         rev: v1.2.4
         hooks:
           - id: cleveref-capitalization
           - id: csquotes
           - id: ensure-labels-for-sections
           - id: no-space-in-cite
           - id: tilde-cite
     ```

     hoặc có thể tải về nội dung của file này [.pre-commit-config.yaml](https://github.com/thiminhnhut/latex/blob/master/latex-and-git/.pre-commit-config.yaml)

  1. Add module `pre-commit` vào project:

     ```bash
     pre-commit install
     ```

  1. Thực hiện quá trình viết nội dung của project như bình thường.

  1. Kiểm tra code của chúng ta đúng quy ước chung hay chưa:

     ```bash
     pre-commit run --all-files
     ```

  1. Khi `commit` lại các thay đổi trong project, `git` sẽ gọi lệnh thực thi
     kiểm tra `hook` (các khai báo, quy ước trong file `.pre-commit-config.yaml`),
     nếu thành công thì `commit` hoàn thành, nếu thất bại thì gợi ý cho chúng ta
     sửa lại, rồi quay lại commit để đảm bảo code đúng quy ước chung.
