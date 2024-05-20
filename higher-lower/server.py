from flask import Flask
import random

app = Flask(__name__)


random_number = random.randint(0, 9)

low_html = '<h1 style=color:red>Too low, try again!</h1>' \
           '<img src=https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif>'
high_html = '<h1 style=color:purple>Too high, try again!</h1>' \
            '<img src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif>'
correct_html = '<h1 style=color:green>You found me!</h1>' \
               '<img src=https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif>'


@app.route("/")
def home_route():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>'


@app.route("/<int:number>")
def output_route(number):
    if number > random_number:
        return high_html
    if number < random_number:
        return low_html
    if number == random_number:
        return correct_html


if __name__ == "__main__":
    app.run(debug=True)
