import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean


app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def get_random_cafe():
    with app.app_context():
        result = db.session.execute(db.select(Cafe))
        all_cafes = result.scalars().all()
        random_cafe = random.choice(all_cafes)
        return jsonify(cafe={
            # "id": random_cafe.id,
            "name": random_cafe.name,
            "map_url": random_cafe.map_url,
            "img_url": random_cafe.img_url,
            "location": random_cafe.location,
            "amenities": {
                "has_sockets": random_cafe.has_sockets,
                "has_toilet": random_cafe.has_toilet,
                "has_wifi": random_cafe.has_wifi,
                "can_take_calls": random_cafe.can_take_calls,
                "seats": random_cafe.seats,
                "coffee_price": random_cafe.coffee_price
            }
        })

@app.route("/all", methods=["GET"])
def all_cafe():
    all_cafes = db.session.execute(db.select(Cafe).order_by(Cafe.name)).scalars().all()
    list_of_cafes = []
    for cafes in all_cafes:
        list_of_cafes.append(cafes.to_dict())
    return jsonify(cafes=list_of_cafes)

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)