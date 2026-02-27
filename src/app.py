from __future__ import annotations

from src.io.parser import parse_input
from src.controller.scheduler import run_scheduling
from src.io.layoutOutput import buildReport


def run(input_path: str, output_path: str) -> None:
    """
    Logic chính của ứng dụng:
    - Bước 1: Đọc file đầu vào (input)
    - Bước 2: Chạy quy trình lập lịch (scheduling)
    - Bước 3: Đưa ra báo cáo thống kê (report)
    - Bước 4: Ghi kết quả ra file
    Được tách riêng khỏi module CLI để dễ dàng tái sử dụng và kiểm thử.
    """
    queues, processes = parse_input(input_path)
    segments, processes = run_scheduling(queues, processes)

    report = buildReport(segments, processes)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report)

