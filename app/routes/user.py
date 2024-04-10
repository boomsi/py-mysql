from flask import Blueprint, request
from werkzeug.security import generate_password_hash, check_password_hash
from ..utils.mysql import mysql
from ..utils.base import Resp
from ..utils.finish_resp import finish_resp

user_bp = Blueprint('user', __name__, url_prefix='/user')

def registry_validate(func):
    pass

@user_bp.route('/registry', methods=('POST',))
def registry():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username:
        return finish_resp(Resp(status_code=0, message='Username is invalide'))
    if not password:
        return finish_resp(Resp(status_code=0, message='Password is invalide'))

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
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username:
        return finish_resp(Resp(status_code=0, message='Username is invalide'))
    if not password:
        return finish_resp(Resp(status_code=0, message='Password is invalide'))

    user = mysql.fetch_one(
        'SELECT * FROM user WHERE username = %s',
        (username,)
    )
    if not user:
        return finish_resp(Resp(status_code=0, message='User does not exist'))

    if not check_password_hash(user.get('password'), password):
        return finish_resp(Resp(status_code=0, message='Password is wrong'))
    
    del user['password']
    return finish_resp(Resp(data=user))