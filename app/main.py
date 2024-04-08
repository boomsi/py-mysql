from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

app.run(port=5001, debug=True)

def start():
    pass