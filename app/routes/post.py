from flask import Blueprint

post_bp = Blueprint('post', __name__, url_prefix='/api/post')


@post_bp.route('/list')
def post_list():
    pass

@post_bp.route('/create')
def post_create():
    pass

@post_bp.route('/update/<int:id>', methods=['PUT'])
def post_update():
    pass

@post_bp.route('/delete/<int:id>', methods=['DELETE'])
def post_delete():
    pass
