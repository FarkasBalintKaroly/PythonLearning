from flask import Flask, render_template
import requests

posts_url = "https://api.npoint.io/674f5423f73deab1e9a7"

all_posts = requests.get(url=posts_url).json()

app = Flask(__name__)


@app.route("/")
def get_all_posts():
    return render_template(template_name_or_list="index.html", posts=all_posts)


@app.route("/about")
def about():
    return render_template(template_name_or_list="about.html")


@app.route("/contact")
def contact():
    return render_template(template_name_or_list="contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for post in all_posts:
        if post["id"] == index:
            requested_post = post
    return render_template(template_name_or_list="post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
