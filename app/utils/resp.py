from dataclasses import dataclass

@dataclass
class Resp:
    status_code: int = 200
    message: str = None
    data: any = None

