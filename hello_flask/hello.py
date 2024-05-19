from flask import Flask

app = Flask(__name__)


def make_bold(function):
    """This decorator function makes an HTML element from a string, that will be bold. (<b></b>)"""
    def wrapper_function():
        text = function()
        bold_text = f"<b>{text}</b>"
        return bold_text
    return wrapper_function


def make_emphasis(function):
    """This decorator function makes an HTML element from a string, that will be italic. (<em></em>)"""
    def wrapper_function():
        text = function()
        italic_text = f"<em>{text}</em>"
        return italic_text
    return wrapper_function


def make_underlined(function):
    """This decorator function makes an HTML element from a string, that will be underlined. (<u></u>)"""
    def wrapper_function():
        text = function()
        underlined_text = f"<u>{text}</u>"
        return underlined_text
    return wrapper_function


@app.route("/")
def hello_world():
    """This function makes the home page of the project."""
    return '<h1 style="text-align:center">Hello, World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://scontent.fbud7-3.fna.fbcdn.net/v/t39.30808-6/434503357_7543104802416693_' \
           '731619986616389855_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=5f2048&_nc_ohc=gK6N-IyUaKoQ7kNvgGFkkXP&' \
           '_nc_ht=scontent.fbud7-3.fna&oh=00_AYACsZHvvIgH0FwdqFanJjw3Xjj5WanhJSjeEDgLfNHOug&oe=664FFB1E" width=700px>'


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_greeting():
    """This function makes a simple page practicing decorators."""
    return "Bye"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    """This function makes a simple page for practicing usages of values."""
    return f"Hello {name}, you are {number} years old!"


if __name__ == "__main__":
    # Run the Flask in debugger mode
    app.run(debug=True)
