from flask import request, g
import jwt
from ..utils.finish_resp import finish_resp
from ..utils.resp import Resp
from ..utils.const import AUTH_WHITE_LIST, JWT_SECRET


def before_request():
    if request.path in AUTH_WHITE_LIST:
        return None

    token = request.headers.get('Authorization')
    if not token:
        return finish_resp(Resp(status_code=0, message='Permission denied'))

    try:
        user = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return finish_resp(Resp(status_code=0, message='Login expired'))
    g.user = user