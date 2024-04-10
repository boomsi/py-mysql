import functools
from flask import request
from ..utils.base import Resp
from ..utils.finish_resp import finish_resp

def params_validate(data: dict):
    def validate(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            req_data = request.get_json()
            for key, value in data.items():
                if not req_data.get(key) or not isinstance(req_data.get(key), value):
                    return finish_resp(Resp(status_code=0, message=f'{key} is invalide'))
            return func(*args, **kwargs)
        return wrapper
    return validate
