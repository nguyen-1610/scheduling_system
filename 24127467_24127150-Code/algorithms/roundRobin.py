
from __future__ import annotations
from typing import Sequence, Any

def pickNextQueue(queuePtr: int, ready: Sequence[Sequence[Any]]) -> int:
    """
    Duyệt thiết lập (Round Robin) chạy xoay vòng giữa các hàng đợi định tuyến (queue):
    - Khởi chạy kiểm tra tại trỏ hàng đợi (queuePtr) và quét lần lượt một vòng tròn
    - Tìm và trả về chỉ số (index) đầu tiên của hàng đợi không trống
    - Điều kiện lý tưởng: hệ thống giả lập gọi hàm này khi chắc chắn tồn tại 
      tối thiểu 1 tiến trình đang sẵn sàng chạy trong danh sách lưới.
    """
    n = len(ready)
    if n == 0:
        raise ValueError("No queues configured")

    for k in range(n):
        q = (queuePtr + k) % n
        if len(ready[q]) > 0:
            return q

    raise ValueError("All queues are empty")