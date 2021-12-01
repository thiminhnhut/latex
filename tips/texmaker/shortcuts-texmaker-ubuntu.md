# Sử dụng phím tắt trong TeXMaker trên Ubuntu 16.04

Thực hiện: Thi Minh Nhựt - Email: thiminhnhut@gmail.com

Thời gian: Ngày 01 tháng 02 năm 2017

## Nguồn tham khảo

[Texmaker Shortcuts not working on Ubuntu 16.04](http://askubuntu.com/questions/786280/texmaker-shortcuts-not-working-on-ubuntu-16-04)

## Vấn đề khi cài đặt TeXMaker trên Ubuntu 16.04

- Khi cài đặt `TeXMaker` trên `Ubuntu 16.04` bằng lệnh `sudo apt-get install texmaker`,
  khi mở giao diện `TeXMaker` thì mặt định không sử dụng được các phím tắt trong `TeXMaker`.

- Để khắc phục vấn đề này chúng ta thực hiện theo hướng dẫn bên dưới.

## Cách thực hiện

- **Bước 1:** Tìm file `texmaker.desktop`:

  ```bash
  $ sudo find / -name texmaker.desktop
  /usr/share/applications/texmaker.desktop
  ```

- **Bước 2:** Mở file `texmaker.desktop`:

  ```bash
  sudo nano /usr/share/applications/texmaker.desktop
  ```

- **Bước 3:** Tìm đến dòng lệnh `Exec=texmaker %F` và thay đổi thành `Exec=env UBUNTU_MENUPROXY= texmaker %F`.
  Nội dung file `texmaker.desktop` sau khi thay đổi như bên dưới:

  ```bash
  [Desktop Entry]

  Categories=Office;Publishing;Qt;X-SuSE-Core-Office;X-Mandriva-Office-Publishing;X-Misc;

  Keywords=Editor;Latex;

  Exec=env UBUNTU_MENUPROXY= texmaker %F

  GenericName=LaTeX Editor

  GenericName[fr]=Editeur LaTeX

  Comment=LaTeX development environment

  Comment[fr]=Environnement de développement LaTeX

  Icon=texmaker

  MimeType=text/x-tex;

  Name=Texmaker

  Name[fr]=Texmaker

  StartupNotify=false

  Terminal=false

  Type=Application
  ```

  Nhấn `Ctrl + X + Y` và `Enter` để lưu và thoát.

- **Kết quả:** Sau khi thực hiện xong các bước trên, chúng ta có thể sử dụng các phím tắt
  trong `TeXMaker` để soạn thảo tài liệu LaTeX trên hệ điều hành Ubuntu 16.04.
