import flask

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route("/en_ny_plats")
def home2():
    return "Hello from en ny plats!"

if __name__ == '__main__':
    app.run(debug=True)


