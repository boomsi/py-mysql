from flask import Blueprint, request
from ..utils.mysql import mysql

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/registry', methods=('POST',))
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    captcha = data.get('captcha')
    if not username:
        return 'Username is invalide'
    if not password:
        return 'Password is invalide'
    if not captcha:
        return 'Captcha is invalide'

    user = mysql.fetch_one(
        'SELECT * FROM user WHERE username = %s',
        (username,)
    )
    
    if user:
        return 'User already exists'

    user = mysql.insert_one(
        'INSERT INTO user (username, password) VALUES (%s, %s)',
        (username, password)
    )

    print(user)
    
    return str(user)


