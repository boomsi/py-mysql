from flask import Blueprint, request, g
from ..utils.params_validate import params_validate
from ..utils.mysql import mysql
from ..utils.finish_resp import finish_resp
from ..utils.resp import Resp

post_bp = Blueprint('post', __name__, url_prefix='/api/post')


@post_bp.route('/list', methods=('GET',))
@params_validate(dict(
    page=dict(type=int, required=False),
    size=dict(type=int, required=False)
))
def post_list():
    page = int(request.args.get('page', 1))
    size = int(request.args.get('size', 10))
    res = mysql.fetch_all(
        'SELECT * FROM post LIMIT %s',
        (page * size,)
    )
    return finish_resp(Resp(data=res))

@post_bp.route('/create', methods=['POST'])
@params_validate(dict(
    title=dict(type=str, required=True),
    content=dict(type=str, required=True)
))
def post_create():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    user_id = g.user.get('id')

    res = mysql.edit_one(
        'INSERT INTO post (title, content, user_id) VALUES (%s, %s, %s)',
        (title, content, user_id)
    )
    return finish_resp(Resp(data=res))


@post_bp.route('/update/<int:id>', methods=['PUT'])
@params_validate(dict(
    title=dict(type=str, required=True),
    content=dict(type=str, required=True)
))
def post_update(id):
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    exist = mysql.fetch_one(
        'SELECT * FROM post WHERE id = %s',
        (id,)
    )

    if not exist:
        finish_resp(Resp(message='Post is not exist'))
    
    data = mysql.edit_one(
        'UPDATE post SET title = %s, content = %s WHERE id = %s',
        (title, content, id)
    )

    return finish_resp(Resp(data=data))

@post_bp.route('/delete/<int:id>', methods=['DELETE'])
def post_delete(id):
    data = mysql.edit_one(
        'DELETE FROM post WHERE id = %s',
        (id,)
    )

    return finish_resp(Resp(data=data))
