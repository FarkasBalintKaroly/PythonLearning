from flask import Flask, render_template
import random
from datetime import datetime
import requests

AGIFY_API_URL = "https://api.agify.io"
GENDERIFY_API_URL = "https://api.genderize.io"


app = Flask(__name__)


def get_age(typed_name):
    params = {"name": typed_name}
    response = requests.get(url=AGIFY_API_URL, params=params)
    age = response.json()["age"]
    return age


def get_gender(typed_name):
    params = {"name": typed_name}
    response = requests.get(url=GENDERIFY_API_URL, params=params)
    gender = response.json()["gender"]
    return gender


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.now().year
    return render_template(template_name_or_list="index.html", num=random_number, current_year=current_year)


@app.route("/<username>")
def guess(username):
    name = username.title()
    age = get_age(name)
    gender = get_gender(name)
    return render_template(template_name_or_list="guess.html", name=name, age=age, gender=gender)


@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    return render_template(template_name_or_list="blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)

