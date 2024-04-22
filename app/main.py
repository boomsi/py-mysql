from flask import Flask
from app.routes.user import user_bp
from app.routes.post import post_bp
from .routes.middleware import before_request

app = Flask(__name__)

@app.route('/')
def index():
    return 'H'

app.before_request(before_request)

app.register_blueprint(user_bp)
app.register_blueprint(post_bp)

app.run(port=5001, debug=True)

def start():
    pass
