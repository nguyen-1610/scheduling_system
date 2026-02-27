from __future__ import annotations

import argparse
from typing import List, Optional

from src.app import run as run_app


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="time-scheduling",
        description="Trình mô phỏng lập lịch CPU với nhiều hàng đợi định tuyến (Round Robin) kết hợp thuật toán SJF/SRTN.",
    )
    parser.add_argument(
        "input_file",
        help="Đường dẫn đến file đầu vào (chứa cấu hình hàng đợi và tiến trình).",
    )
    parser.add_argument(
        "output_file",
        help="Đường dẫn đến file đầu ra (báo cáo kết quả lập lịch).",
    )
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    run_app(args.input_file, args.output_file)
    return 0

