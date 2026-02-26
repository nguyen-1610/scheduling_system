from __future__ import annotations

"""
Điểm chạy chương trình (Entry point) chính thông qua câu lệnh: 
`python -m src.main <FILE_ĐẦU_VÀO> <FILE_ĐẦU_RA>`

Lưu ý:
- Toàn bộ thao tác phân tích dữ liệu lệnh đầu vào (CLI - Command Line Interface) đã được tách sang file `src/cli.py` để dễ tập trung quản lý.
- Chỉ đơn giản là chuyển tiếp (forward) sang hàm main() của CLI và thoát khỏi hệ thống với mã lỗi chuẩn do hệ điều hành cấp.
"""

from src.cli import main as cli_main


if __name__ == "__main__":
    raise SystemExit(cli_main())