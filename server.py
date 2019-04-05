from flask import Flask
app = Flask(__name__)

@app.route('/')
def index_route():
    return '<h1>Welcome.</h1>'

if __name__ == '__main__':
    app.run(host='localhost', port=80, debug=True)