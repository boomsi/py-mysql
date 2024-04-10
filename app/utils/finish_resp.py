from .base import Resp
from typing import Type


def finish_resp(data: any):
    if isinstance(data, Resp):
        return data.__dict__
    else:
        raise TypeError(f'Expect {Type[Resp]}, but got {type(data)}')
