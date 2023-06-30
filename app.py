from flask import Flask


app = Flask(__name__)


@app.route("/hello")
def greeting():
    return "Hello from flask application"
