from flask import Blueprint, request
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import json
from datetime import datetime
from ..utils.mysql import mysql
from ..utils.resp import Resp
from ..utils.finish_resp import finish_resp
from ..utils.params_validate import params_validate
from ..utils.redis import redis
from ..utils.encode import Encoder
from time import sleep
from ..utils.const import JWT_SECRET

user_bp = Blueprint('user', __name__, url_prefix='/api/user')

@user_bp.route('/registry', methods=('POST',))
@params_validate({'username': str, 'password': str})
def registry():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = mysql.fetch_one(
        'SELECT * FROM user WHERE username = %s',
        (username,)
    )
    
    if user:
        return finish_resp(Resp(status_code=0, message='User already exists'))
    user = mysql.insert_one(
        'INSERT INTO user (username, password) VALUES (%s, %s)',
        (username, generate_password_hash(password))
    )
    return finish_resp(Resp(data=user))

@user_bp.route('/login', methods=('POST',))
@params_validate({'username': str, 'password': str})
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = mysql.fetch_one(
        'SELECT * FROM user WHERE username = %s',
        (username,)
    )

    if not user:
        return finish_resp(Resp(status_code=0, message='User does not exist'))
    if not check_password_hash(user.get('password'), password):
        return finish_resp(Resp(status_code=0, message='Password is wrong'))

    # user['created_at'] = user['created_at'].timestamp()
    # user['updated_at'] = user['updated_at'].timestamp()
    del user['password']
    user['exp'] = datetime.now().timestamp() + 24 * 60 * 60

    encoded = jwt.encode(user, JWT_SECRET, algorithm="HS256", json_encoder=Encoder)
    return finish_resp(Resp(data=encoded))

