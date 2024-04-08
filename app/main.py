from flask import Flask
from routes.user import user_bp

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

app.register_blueprint(user_bp)

app.run(port=5001, debug=True)

def start():
    pass