from flask import Blueprint, request
from ..utils.params_validate import params_validate
from ..utils.mysql import mysql
from ..utils.finish_resp import finish_resp
from ..utils.resp import Resp

post_bp = Blueprint('post', __name__, url_prefix='/api/post')


@post_bp.route('/list')
@params_validate({
    'page': {'type': int, 'required': False, 'default': 1},
    'size': {'type': int, 'required': False, 'default': 10},
})
def post_list():
    page = request.args.get('page', 1)
    size = request.args.get('size', 10)
    res = mysql.fetch_all(
        'SELECT * FROM post LIMIT %s, %s',
        (page, size)
    )
    return finish_resp(Resp(data=res))

@post_bp.route('/create')
def post_create():
    pass

@post_bp.route('/update/<int:id>', methods=['PUT'])
def post_update():
    pass

@post_bp.route('/delete/<int:id>', methods=['DELETE'])
def post_delete():
    pass
