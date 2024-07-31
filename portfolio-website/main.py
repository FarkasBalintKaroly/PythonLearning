from flask import Flask, abort, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5


app = Flask(__name__)
Bootstrap5(app)

@app.route('/')
def home():
    return render_template(template_name_or_list='index.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)