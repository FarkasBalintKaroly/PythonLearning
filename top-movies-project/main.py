from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired
import requests
import os


# Required for requests
TOP_MOVIES_API_KEY = os.environ.get("TOP_MOVIES_API_KEY")
SEARCH_FOR_MOVIES_API_ENDPOINT = "https://api.themoviedb.org/3/search/movie"
MOVIE_DETAILS_API_ENDPOINT = "https://api.themoviedb.org/3/movie/"
MOVIE_IMAGE_URL = "https://image.tmdb.org/t/p/w500"


# Creating a form for rating editing
class EditRatingForm(FlaskForm):
    new_rating = FloatField("Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    new_review = StringField("Your Review", validators=[DataRequired()])
    submit_field = SubmitField("Done")

class AddMovieTitle(FlaskForm):
    movie_title = StringField("Movie Title", validators=[DataRequired()])
    submit_field = SubmitField("Add Movie")

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
    year: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String(500))
    rating: Mapped[float] = mapped_column(Float)
    ranking: Mapped[int] = mapped_column(Integer)
    review: Mapped[str] = mapped_column(String(250))
    img_url: Mapped[str] = mapped_column(String(250))

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

@app.route("/add", methods=["POST", "GET"])
def add():
    add_new_movie_form = AddMovieTitle()
    add_new_movie_form.validate_on_submit()
    if add_new_movie_form.validate_on_submit():
        new_title = add_new_movie_form.movie_title.data
        params = {
            "api_key": TOP_MOVIES_API_KEY,
            "query": new_title,
            "language": "en-US"
        }
        response = requests.get(url=SEARCH_FOR_MOVIES_API_ENDPOINT, params=params)
        all_movies = response.json()["results"]
        return render_template(template_name_or_list="select.html", all_movies=all_movies)
    return render_template(template_name_or_list="add.html", form=add_new_movie_form)


@app.route("/find_movie")
def find_movie():
    movie_id = request.args.get("id")
    if movie_id:
        movie_api_url = f"{MOVIE_DETAILS_API_ENDPOINT}/{movie_id}"
        response = requests.get(url=movie_api_url, params={"api_key": TOP_MOVIES_API_KEY})
        new_movie_details = response.json()
        title = new_movie_details["title"]
        img_url = f"{MOVIE_IMAGE_URL}{new_movie_details['poster_path']}"
        year = new_movie_details["release_date"].split("-")[0]
        description = new_movie_details["overview"]
        new_movie = Movie(title=title, img_url=img_url, year=year, description=description)
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
