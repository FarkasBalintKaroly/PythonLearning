from flask import Flask
import os

print(os.environ.get("FLASK_APP"))

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
