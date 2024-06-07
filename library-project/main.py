from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)


# Create database
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"

# Create the extension
db = SQLAlchemy(model_class=Base)
# Initialise the app with the extension
db.init_app(app)


# Create table
class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


# Create table schema in the database
with app.app_context():
    db.create_all()


@app.route('/')
def home():

    # Read all the records of the database
    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.title))
        all_books = result.scalars().all()
        print(all_books)

    return render_template(template_name_or_list="index.html", all_books=all_books)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        rating = float(request.form["rating"])

        # Create a record to the database
        with app.app_context():
            new_book = Book(title=title, author=author, rating=rating)
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))
        # return render_template(template_name_or_list="index.html", all_books=all_books)

    return render_template(template_name_or_list="add.html")


@app.route("/edit_rating/<int:id_>", methods=["POST", "GET"])
def edit_rating(id_):
    print(id_)
    return render_template(template_name_or_list="edit-rating.html")


if __name__ == "__main__":
    app.run(debug=True)
