from flask import Flask, render_template
from post import Post
import requests

# posts_url = "https://api.npoint.io/c790b4d5cab58020d391"
posts_url = "https://api.npoint.io/9e8f160eb8f7f9f27200"
all_posts = requests.get(url=posts_url).json()
post_objects = []
for post in all_posts:
    new_post = Post(post_id=post["id"], title=post["title"], subtitle=post["subtitle"], body=post["body"])
    post_objects.append(new_post)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template(template_name_or_list="index.html", posts=post_objects)


@app.route('/post/<int:blog_id>')
def blog(blog_id):
    return render_template(template_name_or_list='post.html', post=post_objects[blog_id-1])


if __name__ == "__main__":
    app.run(debug=True)
