# src/algorithms/sjf.py
from __future__ import annotations

from typing import List, Tuple
from src.model.entities import Process, Segment


def pop_sjf(ready: List[Process]) -> Process:
    """
    Thuật toán SJF (Shortest Job First): Ưu tiên lấy cái có thời gian xử lý (remaining) ngắn nhất trước.
    Nguyên tắc xử lý các ca trùng số liệu (tie-break):
    Ưu tiên theo thứ tự (remaining -> arrival -> seq).
    """
    if not ready:
        raise ValueError("ready is empty")

    best_idx = 0
    best_key = (ready[0].remaining, ready[0].arrival, ready[0].seq)
    for i in range(1, len(ready)):
        key = (ready[i].remaining, ready[i].arrival, ready[i].seq)
        if key < best_key:
            best_key = key
            best_idx = i

    return ready.pop(best_idx)


def sjf(
    queue_id: str,
    ready: List[Process],
    t: int,
    budget: int,
    segments: List[Segment],
) -> Tuple[int, int]:
    """
    Thực thi 1 lượt thuật toán SJF cho 1 hàng đợi (queue cụ thể).
    (đây là thuật toán không bao hàm ngắt hay gián đoạn: non-preemptive):
    - Dùng thuật toán SJF để lấy một tiến trình lên chạy trực tiếp
    - Thời lượng (dt) sẽ là min của thời lượng công việc (p.remaining) và hạn mức phép chạy của queue (budget)
    - Tạo phân đoạn (Segment) hiển thị cho khoảng thời gian này
    - Cập nhật tiến độ của tiến trình (remaining) và thời điểm kết thúc nếu công việc đã hoàn thành (completion)
    - Nếu vẫn chưa kết thúc nhưng queue đã cạn hạn mức -> Đưa tiến trình vừa rồi nhét lại vào danh sách yêu cầu chờ chạy
    Trả về bộ 2 kết quả: (t_new, budget_left)
    """
    if budget <= 0 or not ready:
        return t, budget

    p = pop_sjf(ready)

    dt = min(p.remaining, budget)
    start = t
    end = t + dt

    segments.append(Segment(start=start, end=end, queue_id=queue_id, pid=p.pid))

    p.remaining -= dt
    t = end
    budget -= dt

    if p.remaining == 0:
        p.completion = t
    else:
        ready.append(p)

    return t, budget