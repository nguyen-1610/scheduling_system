
from dataclasses import dataclass
from typing import Optional, Literal

Policy = Literal["SJF", "SRTN"]

@dataclass
class QueueConfig:
    queue_id: str
    time_slice: int
    policy: Policy

@dataclass
class Process:
    pid: str
    arrival: int
    burst: int
    queue_id: str
    seq: int = 0  # Dùng để phân định trường hợp chỉ số bằng nhau (tie-break), luôn giữ sự ổn định thuận theo dữ liệu đọc từ file đầu tiên

    remaining: int = 0
    completion: Optional[int] = None

    def __post_init__(self):
        # Thiết lập mặc định thời gian còn lại (remaining) bằng thời lượng gốc (burst) nếu khởi tạo đang gán bằng 0
        if self.remaining == 0:
            self.remaining = self.burst

@dataclass
class Segment:
    start: int
    end: int
    queue_id: str
    pid: str