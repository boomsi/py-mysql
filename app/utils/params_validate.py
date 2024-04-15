import functools
from flask import request
from .resp import Resp
from ..utils.finish_resp import finish_resp

'''
data = {
    key: {type: str, required: bool, default: any}
}
'''
def params_validate(data: dict):
    def validate(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            req_data = request.get_json()
            for key, value in data.items():
                if (value.required and not req_data.get(key)) or not isinstance(req_data.get(key), value):
                    return finish_resp(Resp(status_code=0, message=f'{key} is invalide'))
            return func(*args, **kwargs)
        return wrapper
    return validate
