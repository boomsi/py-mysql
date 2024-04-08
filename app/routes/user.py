import functools
from flask import Blueprint, request

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp('/login', methods=('POST',))
def login():
    username = request.form['username']
    password = request.form['password']
    captcha = request.form['captcha']

    error = None

    if not username:
        error = 'Username is invalide'
    if not password:
        error = 'Password is invalide'
    if not captcha:
        error = 'Captcha is invalide'


