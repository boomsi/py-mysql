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
            if request.method in ['GET', 'PATCH']:
                params = request.args
            elif request.is_json:
                params = request.get_json()
            else:
                params = dict()
            
            for key, item in data.items():
                try:
                    value = int(params.get(key)) if item['type'] == int else params.get(key)
                    if (item['required'] and not value) or not isinstance(value, item['type']):
                        return finish_resp(Resp(status_code=0, message=f'{key} is invalide'))
                except ValueError:
                    return finish_resp(Resp(status_code=0, message=f'{key} is invalide'))
            return func(*args, **kwargs)
        return wrapper
    return validate
