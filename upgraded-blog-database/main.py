from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
ckeditor = CKEditor(app)
db.init_app(app)


# Add new post form
class AddNewPostForm(FlaskForm):
    post_title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    blog_img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    blog_content = CKEditorField("Blog Content", validators=[DataRequired()])
    submit_button = SubmitField("SUBMIT NEW POST")


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost).order_by(BlogPost.id))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)


@app.route('/show_post')
def show_post():
    post_id = request.args.get("post_id")
    requested_post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id))
    requested_post = requested_post.scalar()
    return render_template("post.html", post=requested_post)


@app.route('/new-post', methods=["GET", "POST"])
def add_new_post():
    new_post_form = AddNewPostForm()
    if request.method == "POST" and new_post_form.validate:
        title = new_post_form.post_title.data
        subtitle = new_post_form.subtitle.data
        author = new_post_form.author.data
        blog_img_url = new_post_form.blog_img_url.data
        blog_content = new_post_form.blog_content.data
        post_date = date.today().strftime("%B %d, %Y")

        new_post = BlogPost(
            title=title,
            subtitle=subtitle,
            date=post_date,
            body=blog_content,
            author=author,
            img_url=blog_img_url,
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=new_post_form)


# Edit a post
@app.route('/edit-post/<int:post_id>', methods=["POST", "GET"])
def edit_post(post_id):
    return post_id

# TODO: delete_post() to remove a blog post from the database


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
