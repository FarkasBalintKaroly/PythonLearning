from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired
import requests


# Creating a form for rating editing
class EditRatingForm(FlaskForm):
    new_rating = FloatField("Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    new_review = StringField("Your Review", validators=[DataRequired()])
    submit_field = SubmitField("Done")

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"

# CREATE DB
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'

# Create table schema in the database
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    """Home page of the project"""
    # Read all the records of the database
    with app.app_context():
        result = db.session.execute(db.select(Movie).order_by(Movie.id))
        all_movies = result.scalars().all()
    # Load the template webpage with the movies
    return render_template(template_name_or_list="index.html", all_movies=all_movies)

@app.route("/edit", methods=["POST", "GET"])
def edit():
    """Edit a movie rating and review in the database."""
    edit_rating_form = EditRatingForm()
    edit_rating_form.validate_on_submit()
    if edit_rating_form.validate_on_submit():
        new_rating = edit_rating_form.new_rating.data
        new_review = edit_rating_form.new_review.data
        movie_id = request.args.get("id")
        # Update record in the database
        with app.app_context():
            book_to_update = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
            book_to_update.rating = new_rating
            book_to_update.review = new_review
            db.session.commit()
        return redirect(url_for("home"))
    return render_template(template_name_or_list="edit.html", form=edit_rating_form)


@app.route("/delete")
def delete():
    """Delete a movie from the database."""
    movie_id = request.args.get("id")
    movie_to_delete = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
