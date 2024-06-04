from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    return render_template(template_name_or_list="index.html")


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        rating = int(request.form["rating"])
        new_book = {
            "title": title,
            "author": author,
            "rating": rating,
        }
        all_books.append(new_book)
        print(all_books)
    return render_template(template_name_or_list="add.html")


if __name__ == "__main__":
    app.run(debug=True)

